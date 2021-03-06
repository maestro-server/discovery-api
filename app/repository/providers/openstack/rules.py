import json
import re

from pydash.numerical import divide
from pydash.objects import get, pick_by
from pydash.utilities import identity

from app.libs.cache import CacheMemory
from app.repository.externalMaestroData import ExternalMaestroData
from app.services.rules.libs.sync_foreign import sync_apps
from app.services.rules.ruler import Ruler


class RulerOpenStack(Ruler):

    @staticmethod
    def switchRam(source, batch):
        dirts = Ruler.switch(source, batch, [])
        return divide(dirts, 1000)

    @staticmethod
    def fctStorage(source, batch):
        storage = []
        dirts = Ruler.switch(source, batch, [])

        for item in dirts:
            id = get(item, 'id')
            clean = {
                'name': 'vol-%s' % id[0:3],
                'unique_id': id
            }
            storage.append(clean)
        return storage

    @staticmethod
    def fctDc(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('dc_id', source),
            'region': Ruler.switch('region', source),
            'zone': Ruler.switch('availability_zone', batch),
            'type': 'Virtual',
            'instance': Ruler.switch('flavor.id', batch),
            'instance_id': Ruler.switch('id', batch),
            'host_id': Ruler.switch('host_id', batch),
            'hypervisor_hostname': Ruler.switch('hypervisor_hostname', batch),
            'image_id': Ruler.switch('image.id', batch),
            'patch_update': Ruler.switch('patch_update', batch),
            'project_id': Ruler.switch('project_id', batch),
            'service': Ruler.switch('service', batch),
            'user_id': Ruler.switch('user_id', batch),
            'vm_state': Ruler.switch('vm_state', batch),
            'security_groups': Ruler.switch('security_groups', batch),
            'terminated_at': Ruler.switch('terminated_at', batch)
        }
        return pick_by(dc, identity)

    @staticmethod
    def fctDcApp(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('_id', source),
            'region': Ruler.switch('region', source),
            'zone': Ruler.switch('availability_zones', batch)
        }
        return pick_by(dc, identity)

    @staticmethod
    def fctPrivateIp(source, batch):
        dirts = Ruler.switch(source, batch, {})
        if dirts:
            first = next(iter(dirts.values()))
            return get(first, '[0].addr')

    @staticmethod
    def fctPublicIp(source, batch):
        ip = None
        dirts = Ruler.switch(source, batch, {})

        if dirts:
            for key, item in dirts.items():
                key = key.lower()
                if re.search('internet|public', key):
                    ip = get(item, '[0].addr')
                    break

            return ip

    @staticmethod
    def InstanceTypeOpenStack(source, batch, obj={}):
        instance = Ruler.switch(source, batch)

        if instance:
            obj = CacheMemory.get(instance)
            if not obj:
                query = json.dumps({'unique_id': instance})
                result = ExternalMaestroData() \
                    .post_request(path="flavors", body={'query': query}) \
                    .get_results('items')

                if result:
                    content = get(result, '[0]')
                    vcpus = get(content, 'vcpus')
                    memory = get(content, 'memory')

                    if vcpus and memory:
                        obj = {
                            'cpu': RulerOpenStack.getNumbers(vcpus),
                            'memory': RulerOpenStack.getNumbers(memory),
                        }

                        CacheMemory.set(instance, obj)

        return obj

    @staticmethod
    def SyncForeignEntityByTag(source, batch):
        result = []

        tentity = Ruler.switch('metadata.%s' % source, batch)

        if tentity:
            result += sync_apps(tentity, source)

        tentity = Ruler.switch('metadata.%s_id' % source, batch)

        if tentity:
            result += sync_apps(tentity, source, '_id')

        return result

    @staticmethod
    def getNumbers(vcpus):

        if isinstance(vcpus, str):
            return re.search(r'([0-9]*)', vcpus).group()

        if isinstance(vcpus, (int, float)):
            return vcpus
