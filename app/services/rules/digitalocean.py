from hashlib import sha1
from collections import OrderedDict
from .ruler import Ruler
from pydash.objects import pick_by, omit
from pydash.utilities import identity

class RulerDigitalOcean(Ruler):
    @staticmethod
    def getMemory(source, batch):
        memory = Ruler.switch(source, batch, [])

        if memory:
            memory = int(memory)
            return memory/1000


    @staticmethod
    def fctStorage(source, batch):
        storage = []
        dirts = Ruler.switch(source, batch, [])

        for item in dirts:
            clean = {
                'name': 'v-'+item,
                'unique_id': item,
                'status': 'Active'
            }
            storage.append(clean)

        built = Ruler.switch('disk', batch)

        if built:
            storage.append({'size': built, 'name': 'v-built', 'status': 'Active'})

        return storage

    @staticmethod
    def fctDc(source, batch):
        features = batch.get('features', [])

        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('dc_id', source),
            'region': Ruler.switch('region.slug', batch),
            'available': Ruler.switch('region.available', batch),
            'type': 'Virtual',
            'instance': Ruler.switch('size_slug', batch),
            'instance_id': Ruler.switch('id', batch),

            'price_monthly': Ruler.switch('size.price_monthly', batch),
            'price_hourly': Ruler.switch('size.price_hourly', batch),

            'kernel': Ruler.switch('kernel', batch),

            'monitoring': Ruler.setV("monitoring" in features),
            'backups': Ruler.setV("backups" in features),

            'virtio': Ruler.setV("virtio" in features),
            'storage': Ruler.setV("storage" in features),
            'image_transfer': Ruler.setV("image_transfer" in features),
            'install_agent': Ruler.setV("install_agent" in features),

            'ipv6': Ruler.setV("ipv6" in features),
            'private_networking': Ruler.setV("private_networking" in features)
        }
        return pick_by(dc, identity)

    @staticmethod
    def fctDcBuckets(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('dc_id', source),
            'region': Ruler.switch('region', source)
        }
        return pick_by(dc, identity)

    @staticmethod
    def fctPrivateIp(source, batch):
        ips = Ruler.switch(source, batch, [])

        for net in ips:
            if net['type'] == 'private':
                return net['ip_address']

    @staticmethod
    def fctPublicIp(source, batch):
        ips = Ruler.switch(source, batch, [])

        for net in ips:
            if net['type'] == 'public':
                return net['ip_address']

    @staticmethod
    def checksum(source, batch):
        batch = omit(batch, ['checksum', 'backup_ids', 'next_backup_window'])
        dsort = OrderedDict(sorted(batch.items(), key=lambda x: x[0]))
        return sha1(repr(dsort).encode('utf-8')).hexdigest()