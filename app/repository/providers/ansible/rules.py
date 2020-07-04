import re
from app.services.rules.ruler import Ruler
from pydash.objects import get, pick_by, omit
from pydash.utilities import identity
from .helper.makeStorageUniqueId import makeStorageUniqueId
from app.repository.libs.storageSizeConverter import multiple_ten


class RulerAnsible(Ruler):
    @staticmethod
    def getOs(source, batch):

        return {
            "base": batch.get("ansible_system"),
            "dist": batch.get("ansible_distribution"),
            "file_path": batch.get("ansible_distribution_file_path"),
            "variety": batch.get("ansible_distribution_file_variety"),
            "major_version": batch.get("ansible_distribution_major_version"),
            "version": batch.get("ansible_distribution_version")
        }

    @staticmethod
    def getMemory(source, batch):
        return round(int(Ruler.switch(source, batch)) / 1000)

    @staticmethod
    def getAuth(source, batch):
        return [{
            "username": Ruler.switch('ansible_user_id', batch)
        }]

    @staticmethod
    def getService(source, batch):
        return [{
            "name": "Python",
            "version": Ruler.switch('ansible_python_version', batch),
            "status": "Active"
        }]

    @staticmethod
    def fctDc(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            '_id': Ruler.switch('dc_id', source),
            'kernel': Ruler.switch('ansible_kernel', batch),

            'instance': Ruler.switch('ansible_product_name', batch),
            'vendor': Ruler.switch('ansible_system_vendor', batch),
            'virtualization': Ruler.switch('ansible_virtualization_type', batch),
            'architecture': Ruler.switch('ansible_architecture', batch),
            'bios_date': Ruler.switch('ansible_bios_date', batch)

        }
        return pick_by(dc, identity)

    @staticmethod
    def getStorages(source, batch):
        storages = []
        data = Ruler.switch(source, batch, {})

        for key, value in data.items():
            storage = {
                'name': key,
                'partitions': RulerAnsible.getPartitions(batch, value.get('partitions', [])),
                'unique_id': makeStorageUniqueId(key, value).make(),
                'status': 'attached'
            }
            storages.append(storage)

        return storages

    @staticmethod
    def getPartitions(batch, device):
        partitions = []
        for key, value in device.items():
            uuid = Ruler.switch('uuid', value)
            more = RulerAnsible.getSingleMount(batch.get('ansible_mounts', []), uuid)
            partition = {
                'name': key,
                'size': RulerAnsible.getSize('size', value),
                'uuid': uuid
            }
            partitions.append({**partition, **more})

        return partitions

    @staticmethod
    def getSize(source, batch):
        size = Ruler.switch(source, batch)
        multipler = re.search(r'[A-Z]{2}', size).group()
        ss = int(re.search(r'\d+', size).group())

        return multiple_ten(ss, multipler)

    @staticmethod
    def getUniqueId(_, batch):
        key = Ruler.switch('_key', batch)
        return makeStorageUniqueId(key, batch).make()

    @staticmethod
    def getSingleMount(source, uuid):
        for value in source:
            myuuid = get(value, 'uuid', get(value, 'links.uuids[0]'))
            if myuuid == uuid:
                return {
                    'device': value.get('device'),
                    'mount': value.get('mount'),
                    'ftype': value.get('fstype'),
                    'options': value.get('options')
                }
        return {}

    @staticmethod
    def checksum(source, batch):
        batch = omit(batch, ['checksum'])
        return Ruler.checksum(source, batch)
