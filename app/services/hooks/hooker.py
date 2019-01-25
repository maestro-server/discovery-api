
from .azure import HookedAzure
from .aws import HookedAWS

class Hooker(object):
    _register = {"Azure": HookedAzure, "AWS": HookedAWS}

    def __init__(self, rules, conn):
        self._rules = rules
        self._conn = conn

    def exec(self, rule, obj):
        hook = rule.get('hook')
        method = rule.get('method')

        return getattr(self._register[hook], method)(obj, self._conn)

    def rules(self, obj):

        for rule in self._rules:
            key = rule.get('key')
            val = self.exec(rule, obj)
            if isinstance(val, dict):
                obj.update(val)
                break

            if val:
                obj[key] = val

    def apply(self, obj):

        if self._rules:
            self.rules(obj)

        return obj

    def run(self, objs):

        if self._rules:
            return [self.apply(obj) for obj in objs]
