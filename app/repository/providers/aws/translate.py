from pydash.objects import get
from app.services.translate.mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.repository.providers.aws.rules import RulerAWS

from app.repository.providers.aws.aws_mapper import *


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
            'list_layers': rules_aws_list_layers(conn),
            'list_queues': rules_list_queues(conn),
            'describe_cache_clusters': rules_describe_cache_clusters(conn),
            'list_identities': rules_list_identities(conn),
            'describe_domains': rules_describe_domains(conn),
            'list_tables': rules_list_tables(conn),
            'get_rest_apis': rules_get_rest_apis(conn),
            'get_apis': rules_get_apis(conn)
        }

        return mapper[command]
