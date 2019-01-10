from pydash.objects import get
from .mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.services.rules.digitalocean import RulerDigitalOcean

from .digitalocean_mapper.do_list_buckets import rules as rules_do_list_buckets


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
