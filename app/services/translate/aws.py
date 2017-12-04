from pydash.objects import get
from .mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.services.rules.aws import RulerAWS

from .aws_mapper.aws_describe_instances import rules as rules_aws_describe_instances
from .aws_mapper.aws_describe_load_balancers import rules as rules_aws_describe_load_balancers
from .aws_mapper.aws_describe_volumes import rules as rules_aws_describe_volumes
from .aws_mapper.aws_list_buckets import rules as rules_aws_list_buckets
from .aws_mapper.aws_describe_images import rules as rules_aws_describe_images

from .aws_mapper.aws_describe_vpcs import rules as rules_aws_describe_vpcs
from .aws_mapper.aws_describe_subnets import rules as rules_aws_describe_subnets
from .aws_mapper.aws_describe_vpc_peering_connections import rules as rules_aws_describe_vpc_peering_connections


from .aws_mapper.aws_describe_vpn_gateways import rules as rules_aws_describe_vpn_gateways
from .aws_mapper.aws_describe_vpc_endpoints import rules as rules_aws_describe_vpc_endpoints
from .aws_mapper.aws_describe_route_tables import rules as rules_aws_describe_route_tables
from .aws_mapper.aws_describe_network_interfaces import rules as rules_aws_describe_network_interfaces
from .aws_mapper.aws_describe_nat_gateways import rules as rules_aws_describe_nat_gateways
from .aws_mapper.aws_describe_network_acls import rules as rules_aws_describe_network_acls
from .aws_mapper.aws_describe_security_groups import rules as rules_aws_describe_security_groups
from .aws_mapper.aws_describe_snapshots import rules as rules_aws_describe_snapshots


class MapperAWS(Mapper):
    def translate(self, data):
        transformed = []

        if self._result_path:
            data = get(data, self._result_path)

        if not isinstance(data, list):
            data = [data]


        for sub in data:
            items = self.mapp(self.command, self.conn).items()
            nw = IteratorRuler().batch(items=items, Ruler=RulerAWS, source=sub)
            transformed.append(nw)

        return transformed

    def mapp(self, command, conn):
        mapper = {
            'describe_instances': rules_aws_describe_instances(conn),
            'describe_load_balancers': rules_aws_describe_load_balancers(conn),
            'list_buckets': rules_aws_list_buckets(conn),
            'describe_volumes': rules_aws_describe_volumes(conn),
            'describe_images': rules_aws_describe_images(conn),
            'describe_snapshots': rules_aws_describe_snapshots(conn),
            'describe_vpcs': rules_aws_describe_vpcs(conn),
            'describe_subnets': rules_aws_describe_subnets(conn),
            'describe_vpc_peering_connections': rules_aws_describe_vpc_peering_connections(conn),
            'describe_vpn_gateways': rules_aws_describe_vpn_gateways(conn),
            'describe_vpc_endpoints': rules_aws_describe_vpc_endpoints(conn),
            'describe_route_tables': rules_aws_describe_route_tables(conn),
            'describe_network_interfaces': rules_aws_describe_network_interfaces(conn),
            'describe_nat_gateways': rules_aws_describe_nat_gateways(conn),
            'describe_network_acls': rules_aws_describe_network_acls(conn),
            'describe_security_groups': rules_aws_describe_security_groups(conn),
        }

        return mapper[command]
