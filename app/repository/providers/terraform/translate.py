from app.services.translate.mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.repository.providers.terraform.rules import RulerTerraform

from app.repository.providers.terraform.terraform_mapper import *


class MapperTerraform(Mapper):

    def translate(self, data):
        transformed = []

        items = self.mapp().items()
        nw = IteratorRuler().batch(items=items, Ruler=RulerTerraform, source=data).result()
        transformed.append(nw)

        return transformed

    def mapp(self):
        mapper = {
            'statefile_instances': rules_terraform_servers(self.conn),
            'statefile_volumes': rules_terraform_volumes(self.conn),
            'statefile_ebs': rules_terraform_storage(self.conn)
        }

        return mapper[self.command]
