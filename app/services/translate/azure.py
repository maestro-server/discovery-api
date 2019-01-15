from pydash.objects import get
from .mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.services.rules.azure import RulerAzure

from .azure_mapper.az_virtual_machines import rules as rules_az_virtual_machine
from .azure_mapper.az_disks import rules as rules_disks
from .azure_mapper.az_network_interfaces import rules as rules_network_interfaces
from .azure_mapper.az_public_ip_addresses import rules as rules_public_ip_addresses
from .azure_mapper.az_route_tables import rules as rules_route_tables
from .azure_mapper.az_virtual_networks import rules as rules_virtual_networks
from .azure_mapper.az_snapshots import rules as rules_snapshots
from .azure_mapper.az_images import rules as rules_images


class MapperAzure(Mapper):
    def translate(self, data):
        transformed = []

        if self._result_path:
            data = get(data, self._result_path)

        if not isinstance(data, list):
            data = [data]

        for sub in data:
            items = self.mapp(self.command, self.conn).items()
            nw = IteratorRuler().batch(items=items, Ruler=RulerAzure, source=sub).result()
            transformed.append(nw)

        return transformed

    def mapp(self, command, conn):
        mapper = {
            'virtual_machines': rules_az_virtual_machine(conn),
            'disks': rules_disks(conn),
            'network_interfaces': rules_network_interfaces(conn),
            'public_ip_addresses': rules_public_ip_addresses(conn),
            'route_tables': rules_route_tables(conn),
            'virtual_networks': rules_virtual_networks(conn),
            'snapshots': rules_snapshots(conn),
            'images': rules_images(conn),
        }

        return mapper[command]
