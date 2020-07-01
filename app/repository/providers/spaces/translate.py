from pydash.objects import get
from app.services.translate.mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.repository.providers.digitalocean.rules import RulerDigitalOcean

from app.repository.providers.spaces.spaces_mapper import *


class MapperSpaces(Mapper):
    def translate(self, data):
        transformed = []

        if self._result_path:
            data = get(data, self._result_path)

        if not isinstance(data, list):
            data = [data]


        for sub in data:
            items = self.mapp(self.command, self.conn).items()
            nw = IteratorRuler().batch(items=items, Ruler=RulerDigitalOcean, source=sub).result()
            transformed.append(nw)


        return transformed

    def mapp(self, command, conn):
        mapper = {
            'list_buckets': rules_do_list_buckets(conn)
        }

        return mapper[command]
