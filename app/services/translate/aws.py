from pydash.objects import get
from .mapper import Mapper
from app.services.iterators.iRuler import IteratorRuler
from app.services.rules.aws import RulerAWS

from .aws_mapper.aws_describe_instances import rules as rules_aws_describe_instances
from .aws_mapper.aws_describe_load_balancers import rules as rules_aws_describe_load_balancers
from .aws_mapper.aws_list_buckets import rules as rules_aws_list_buckets


class MapperAWS(Mapper):
    def translate(self, data):
        if self._result_path:
            data = get(data, self._result_path)

        oper = self.mapp()
        items = oper.items()
        return IteratorRuler().batch(items=items, Ruler=RulerAWS, source=data)

    def mapp(self):
        mapper = {
            'describe_instances': rules_aws_describe_instances(self.conn),
            'describe_load_balancers': rules_aws_describe_load_balancers(self.conn),
            'list_buckets': rules_aws_list_buckets(self.conn)
        }

        return mapper[self.command]
