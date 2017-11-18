
import re
from pydash.objects import get
from app.repository.model import Model
from app.services.iterators.iRuler import IteratorRuler
import datetime

class Ruler(object):

    @staticmethod
    def searchID(key, rule):
        id = re.search('(^_id)|(\._id)', key)

        if id:
            return Ruler.makeObjectId(key, rule)

        return rule

    @staticmethod
    def searchAt(key, rule):
        time = re.search('_at', key)

        if time:
            return datetime.datetime.strptime(rule[:19]+'Z', "%Y-%m-%dT%H:%M:%SZ")

        return rule

    @staticmethod
    def makeObjectId(key, rule):
        if isinstance(rule, list):
            arr = map(lambda x: Ruler.searchID(key, x), rule)
            return list(arr)

        return Model.castObjectId(rule)

    @staticmethod
    def translateLists(key, rule):
        if isinstance(rule, list):
            rule = {'$in': rule}

        return rule

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
                return item[source['catcher']]

    @staticmethod
    def switchOptions(source, batch):
        sts = get(batch, source['field'])
        return get(source['options'], sts, source['default'])

    @staticmethod
    def fctOwner(source, batch):
        return {
            'refs': 'providers',
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
    def batch(source, batch):
        items = source.items()
        return IteratorRuler().batch(items=items, Ruler=Ruler, source=batch)
