from app.services.translate.mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.repository.providers.ansible.rules import RulerAnsible

from app.repository.providers.ansible.ansible_mapper import *


class MapperAnsible(Mapper):
    def translate(self, data):
        transformed = []

        items = self.mapp().items()
        nw = IteratorRuler().batch(items=items, Ruler=RulerAnsible, source=data).result()
        transformed.append(nw)

        return transformed

    def mapp(self):
        mapper = {
            'ansible_facts': rules_ansible_servers(self.conn),
            'ansible_devices': rules_ansible_devices(self.conn)
        }

        return mapper[self.command]
