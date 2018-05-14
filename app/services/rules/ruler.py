import json
from pydash.objects import get
from app.services.iterators.iRuler import IteratorRuler

class Ruler(object):

    @staticmethod
    def setV(source, batch):
        return source

    @staticmethod
    def switch(source, batch, default=None):
        return get(batch, source, default)

    @staticmethod
    def arrCatcher(source, batch):
        list = get(batch, source['field'], [])
        for item in list:
            if item[source['sKey']].lower() == source['s'].lower():
                return item[source['catcher']].capitalize()

    @staticmethod
    def switchOptions(source, batch):
        sts = get(batch, source['field'])
        return get(source['options'], sts, source['default'])

    @staticmethod
    def fctOwner(source, batch):
        return {
            'refs': 'connections',
            'name': Ruler.switch('dc', source),
            '_id': Ruler.switch('_id', source)
        }

    @staticmethod
    def fctAuth(source, batch):
        key = Ruler.switch(source, batch)

        if key:
            return [{'name': key, 'type': 'PKI'}]

    @staticmethod
    def fctRoles(source, batch):
        return get(source, 'roles')

    @staticmethod
    def checksum(source, batch):
        return hash(repr(batch))

    @staticmethod
    def batch(source, batch):
        items = source.items()
        return IteratorRuler().batch(items=items, Ruler=Ruler, source=batch).result()
