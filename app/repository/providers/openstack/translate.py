
from app.services.translate.mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.repository.providers.openstack.rules import RulerOpenStack

from app.repository.providers.openstack.openstack_mapper import *


class MapperOpenStack(Mapper):
    def translate(self, data):
        transformed = []

        items = self.mapp().items()
        nw = IteratorRuler().batch(items=items, Ruler=RulerOpenStack, source=data).result()
        transformed.append(nw)

        return transformed

    def mapp(self):
        mapper = {
            'servers': rules_openstack_servers(self.conn),
            'load_balancers': rules_openstack_loadbalancers(self.conn),
            'routers': rules_openstack_routes(self.conn),
            'networks': rules_openstack_networks(self.conn),
            'ports': rules_openstack_ports(self.conn),
            'subnets': rules_openstack_subnets(self.conn),
            'security_groups': rules_security_groups(self.conn),
            'images': rules_openstack_images(self.conn),
            'snapshots': rules_openstack_snapshots(self.conn),
            'flavors': rules_openstack_flavors(self.conn),
            'volumes': rules_openstack_volumes(self.conn)
        }

        return mapper[self.command]
