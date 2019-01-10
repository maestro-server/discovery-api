
from .mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.services.rules.digitalocean import RulerDigitalOcean

from .digitalocean_mapper.do_get_all_droplets import rules as rules_do_get_all_droplets
from .digitalocean_mapper.do_get_all_volumes import rules as rules_do_get_all_volumes
from .digitalocean_mapper.do_get_my_images import rules as rules_do_get_my_images
from .digitalocean_mapper.do_get_all_load_balancers import rules as rules_get_all_load_balancers
from .digitalocean_mapper.do_get_all_firewalls import rules as rules_get_all_firewalls
from .digitalocean_mapper.do_get_all_cdns import rules as rules_get_all_cdns
from .digitalocean_mapper.do_get_all_kubernetes import rules as rules_get_all_kubernetes

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
