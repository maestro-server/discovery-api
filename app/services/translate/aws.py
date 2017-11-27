from pydash.objects import get
from .mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.services.rules.aws import RulerAWS

from .aws_mapper.aws_describe_instances import rules as rules_aws_describe_instances
from .aws_mapper.aws_describe_load_balancers import rules as rules_aws_describe_load_balancers
from .aws_mapper.aws_list_buckets import rules as rules_aws_list_buckets


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
            'list_buckets': rules_aws_list_buckets(conn)
        }

        return mapper[command]
