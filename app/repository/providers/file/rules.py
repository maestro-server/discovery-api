from app.services.rules.ruler import Ruler
from pydash.objects import pick_by, omit
from pydash.utilities import identity


class RulerFile(Ruler):

    @staticmethod
    def fctDc(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            '_id': Ruler.switch('dc_id', source),
            'zone': Ruler.switch('datacenters.zone', batch),
            'region': Ruler.switch('datacenters.region', batch)
        }
        return pick_by(dc, identity)

    @staticmethod
    def checksum(source, batch):
        batch = omit(batch, ['checksum'])
        return Ruler.checksum(source, batch)
