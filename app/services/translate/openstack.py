
from .mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.services.rules.openstack import RulerOpenStack

from .openstack_mapper.openstack_servers import rules as rules_openstack_servers
from .openstack_mapper.openstack_loadbalancers import rules as rules_openstack_loadbalancers

from .openstack_mapper.openstack_routers import rules as rules_openstack_routes
from .openstack_mapper.openstack_networks import rules as rules_openstack_networks
from .openstack_mapper.openstack_ports import rules as rules_openstack_ports
from .openstack_mapper.openstack_subnets import rules as rules_openstack_subnets
from .openstack_mapper.openstack_security_groups import rules as rules_security_groups

from .openstack_mapper.openstack_images import rules as rules_openstack_images
from .openstack_mapper.openstack_snapshots import rules as rules_openstack_snapshots
from .openstack_mapper.openstack_flavors import rules as rules_openstack_flavors
from .openstack_mapper.openstack_volumes import rules as rules_openstack_volumes


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
