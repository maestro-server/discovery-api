from app.services.translate.mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.repository.providers.file.rules import RulerFile

from app.repository.providers.file.file_mapper import *


class MapperFile(Mapper):
    def translate(self, data):
        transformed = []

        items = self.mapp().items()
        nw = IteratorRuler().batch(items=items, Ruler=RulerFile, source=data).result()
        transformed.append(nw)

        return transformed

    def mapp(self):
        mapper = {
            'maestro_template': rules_servers(self.conn),
            'maestro_applications': rules_applications(self.conn),
            'maestro_volumes': rules_volumes(self.conn),
            'maestro_snapshots': rules_snapshots(self.conn),
            'maestro_images': rules_images(self.conn),
            'maestro_flavors': rules_flavors(self.conn)
        }

        return mapper[self.command]
