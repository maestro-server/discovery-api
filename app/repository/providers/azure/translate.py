from pydash.objects import get
from app.services.translate.mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.repository.providers.azure.rules import RulerAzure

from app.repository.providers.azure.azure_mapper import *


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
