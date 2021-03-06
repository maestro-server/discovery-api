from hashlib import sha1
import re
from app.services.rules.ruler import Ruler
from pydash.objects import pick_by
from pydash.utilities import identity


class RulerAzure(Ruler):
    @staticmethod
    def getMemory(source, batch):
        memory = Ruler.switch(source, batch, [])

        if memory:
            memory = int(memory)
            return memory / 1000

    @staticmethod
    def fcStorage(source, batch):
        storages = []
        data = Ruler.switch(source, batch, [])

        attached = Ruler.switch('data_disks', data)
        if attached:
            for item in attached:
                clean = RulerAzure.fcSingleStorage(item)
                storages.append(clean)

        built = Ruler.switch('os_disk', data)
        if built:
            storages.append(RulerAzure.fcSingleStorage(built))

        return storages

    @staticmethod
    def fcSingleStorage(built):
        data = {
            'size': Ruler.switch('disk_size_gb', built),
            'name': Ruler.switch('name', built),
            'unique_id': RulerAzure.createID(
                {
                    'key': 'managed_disk.id',
                    'reg': r'^\/subscriptions/(.*)/resourceGroups/(.*)/providers/Microsoft.Compute/disks/(.*)?'
                }, built),
            'storage_account_type': Ruler.switch('managed_disk.storage_account_type', built),
            'write_accelerator_enabled': Ruler.switch('write_accelerator_enabled', built),
            'vhd': Ruler.switch('vhd', built),
            'diff_disk_settings': Ruler.switch('diff_disk_settings', built),
            'create_option': Ruler.switch('name', built),
            'status': 'Active'
        }
        return pick_by(data, identity)

    @staticmethod
    def fctDc(source, batch):

        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('dc_id', source),
            'region': Ruler.switch('location', batch),
            'zones': Ruler.switch('zones', batch),

            'instance': Ruler.switch('hardware_profile.vm_size', batch),
            'type': 'Virtual',
            'resource': Ruler.switch('type', batch),
            'instance_id': Ruler.switch('vm_id', batch),
            'license_type': Ruler.switch('license_type', batch)
        }
        return pick_by(dc, identity)

    @staticmethod
    def fcOS(source, batch):
        disk = Ruler.switch(source, batch)
        os = {
            'base': Ruler.switch('os_disk.os_type', disk),
            'dist': Ruler.switch('image_reference.offer', disk),
            'version': Ruler.switch('image_reference.sku', disk)
        }
        return os

    @staticmethod
    def createID(source, batch):
        data = Ruler.switch(source['key'], batch)
        lst = re.findall(source['reg'], data)
        if lst:
            id = '_'.join(str(i) for i in lst[0])
            return sha1(id.encode()).hexdigest()

    @staticmethod
    def serialize(source, batch):
        data = Ruler.switch(source, batch)

        if isinstance(data, list):
            data = [x.serialize() for x in data]

        if hasattr(data, 'serialize'):
            data = data.serialize()

        return data

    @staticmethod
    def checksum(source, batch):
        serialized = batch.serialize()
        return Ruler.checksum(source, serialized)
