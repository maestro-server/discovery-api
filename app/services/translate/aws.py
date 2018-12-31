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
from .aws_mapper.aws_describe_cdns import rules as rules_describe_cdns
from .aws_mapper.aws_describe_db_list import rules as rules_describe_db_list
from .aws_mapper.aws_describe_autoscaling_group import rules as rules_describe_autoscaling_group
from .aws_mapper.aws_describe_scaling_plans import rules as rules_aws_describe_scaling_plans
from .aws_mapper.aws_describe_cdns_rtmp import rules as rules_aws_describe_cdns_rtmp

from .aws_mapper.aws_list_functions import rules as rules_aws_list_functions
from .aws_mapper.aws_list_layers import rules as rules_aws_list_layers


class MapperAWS(Mapper):
    def translate(self, data):
        transformed = []

        if self._result_path:
            data = get(data, self._result_path)

        if not isinstance(data, list):
            data = [data]


        for sub in data:
            items = self.mapp(self.command, self.conn).items()
            nw = IteratorRuler().batch(items=items, Ruler=RulerAWS, source=sub).result()
            transformed.append(nw)


        return transformed

    def mapp(self, command, conn):
        mapper = {
            'describe_instances': rules_aws_describe_instances(conn),
            'describe_load_balancers': rules_aws_describe_load_balancers(conn),
            'list_distributions': rules_describe_cdns(conn),
            'list_streaming_distributions': rules_aws_describe_cdns_rtmp(conn),
            'describe_db_instances': rules_describe_db_list(conn),
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
            'describe_auto_scaling_groups': rules_describe_autoscaling_group(conn),
            'describe_scaling_plans': rules_aws_describe_scaling_plans(conn),
            'list_functions': rules_aws_list_functions(conn),
            'list_layers': rules_aws_list_layers(conn)
        }

        return mapper[command]
