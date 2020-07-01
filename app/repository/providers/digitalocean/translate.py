from app.services.translate.mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.repository.providers.digitalocean.rules import RulerDigitalOcean

from app.repository.providers.digitalocean.digitalocean_mapper import *


class MapperDO(Mapper):

    def translate(self, data):
        transformed = []

        items = self.mapp().items()
        nw = IteratorRuler().batch(items=items, Ruler=RulerDigitalOcean, source=data).result()
        transformed.append(nw)

        return transformed

    def mapp(self):
        mapper = {
            'get_all_droplets': rules_do_get_all_droplets(self.conn),
            'get_all_volumes': rules_do_get_all_volumes(self.conn),
            'get_my_images': rules_do_get_my_images(self.conn),
            'get_all_load_balancers': rules_get_all_load_balancers(self.conn),
            'get_all_snapshots': rules_do_get_my_images(self.conn),
            'get_all_firewalls': rules_get_all_firewalls(self.conn),
            'get_all_kubernetes': rules_get_all_kubernetes(self.conn),
            'get_all_cdns': rules_get_all_cdns(self.conn)
        }

        return mapper[self.command]
