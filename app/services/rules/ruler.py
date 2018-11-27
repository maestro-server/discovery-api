
from hashlib import sha1
from pydash.objects import get
from app.services.iterators.iRuler import IteratorRuler

class Ruler(object):

    @staticmethod
    def setV(source, batch):
        return source

    @staticmethod
    def switch(source, batch, default=None):
        fields = source.split('|')
        for field in fields:
            result = get(batch, field)
            if result:
                return result

        return default

    @staticmethod
    def arrMultiCatcher(source, batch):
        items = source['s']
        for item in items:
            nsr = {**source, **{'s': item}}
            vl = Ruler.arrCatcher(nsr, batch)
            if vl:
                return vl

    @staticmethod
    def arrCatcher(source, batch, cap=True):
        list = get(batch, source['field'], [])
        for item in list:
            if item[source['sKey']].lower() == source['s'].lower():
                tmp = item[source['catcher']]

                if cap:
                    tmp = tmp.capitalize()

                return tmp

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
        return sha1(repr(batch).encode('utf-8')).hexdigest()

    @staticmethod
    def batch(source, batch):
        items = source.items()
        return IteratorRuler().batch(items=items, Ruler=Ruler, source=batch).result()
