
import re
from .ruler import Ruler
from pydash.objects import get

class RulerOpenStack(Ruler):

    @staticmethod
    def fctStorage(source, batch):
        storage = []
        dirts = Ruler.switch(source, batch, [])

        for item in dirts:
            clean = {
                'volume_id': get(item, 'id')
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
        return dc

    @staticmethod
    def fctDcApp(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('_id', source),
            'region': Ruler.switch('region', source),
            'zone': Ruler.switch('availability_zones', batch)
        }
        return dc

    @staticmethod
    def fctTags(source, batch):
        tags = []
        dirts = Ruler.switch(source, batch, {})

        for key, item in dirts.items():
            clean = {
                'key': key,
                'value': item
            }
            tags.append(clean)
        return tags

    @staticmethod
    def fctPrivateIp(source, batch):
        dirts = Ruler.switch(source, batch, {})
        first = next(iter(dirts.values()))

        return get(first, '[0].addr')

    @staticmethod
    def fctPublicIp(source, batch):
        ip = None
        dirts = Ruler.switch(source, batch, {})

        for key, item in dirts.items():
            key = key.lower()
            if re.search('internet|public', key):
                ip = get(item, '[0].addr')
                break

        return ip