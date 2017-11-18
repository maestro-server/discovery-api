
from .mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.services.rules.openstack import RulerOpenStack

from .openstack_mapper.openstack_servers import rules as rules_openstack_servers
from .openstack_mapper.openstack_servers import rules as rules_openstack_loadbalancers


class MapperOpenStack(Mapper):
    def translate(self, data):
        transformed = []

        items = self.mapp().items()
        nw = IteratorRuler().batch(items=items, Ruler=RulerOpenStack, source=data)
        transformed.append(nw)

        return transformed

    def mapp(self):
        mapper = {
            'servers': rules_openstack_servers(self.conn),
            'load_balancers': rules_openstack_loadbalancers(self.conn)
        }

        return mapper[self.command]
