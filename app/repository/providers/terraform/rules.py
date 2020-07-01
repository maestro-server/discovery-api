from app.services.rules.ruler import Ruler
from pydash.objects import pick_by, omit
from pydash.utilities import identity
from app.services.rules.libs.sync_foreign import sync_apps


class RulerTerraform(Ruler):

    @staticmethod
    def fctDc(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            'zone': Ruler.switch('attributes.availability_zone', batch),
            '_id': Ruler.switch('dc_id', source),
            'instance': Ruler.switch('attributes.instance_type', batch),
            'instance_id': Ruler.switch('attributes.id', batch),
            'vpc_security_group_ids': Ruler.switch('attributes.vpc_security_group_ids', batch),
            'subnet_id': Ruler.switch('attributes.subnet_id', batch),
            'arn': Ruler.switch('attributes.arn', batch),
            'image_id': Ruler.switch('attributes.ami', batch),
        }
        return pick_by(dc, identity)

    @staticmethod
    def SyncForeignEntityByTag(source, batch):
        result = []

        opts = {'call': 'switch', 'source': 'tags.applications'}
        tentity = Ruler.switch(opts, batch)

        if tentity:
            result += sync_apps(tentity, source)

        opts = {'call': 'switch', 'source': 'tags.applications_id'}
        tentity = Ruler.switch(opts, batch)

        if tentity:
            result += sync_apps(tentity, source, '_id')

        return result

    @staticmethod
    def fctAuth(source, batch):
        key = Ruler.switch(source, batch)

        if key:
            return [{'name': key, 'type': 'PKI'}]

    @staticmethod
    def fctStorage(source, batch):

        bag = []
        fields = source.split('|')
        for field in fields:
            lst = Ruler.switch(field, batch, [])
            bag.extend(lst)

        storage = []
        for item in bag:
            clean = {
                'device_name': item.get('device_name'),
                'delete_termination': item.get('delete_on_termination'),
                'unique_id': item.get('volume_id')
            }
            storage.append(pick_by(clean, identity))
        return storage

    @staticmethod
    def checksum(source, batch):
        batch = omit(batch, ['checksum'])
        return Ruler.checksum(source, batch)
