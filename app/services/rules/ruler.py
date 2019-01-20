
import datetime
from hashlib import sha1
from pydash.objects import get
from collections import OrderedDict
from .libs.sync_foreign import sync_apps
from app.services.iterators.iRuler import IteratorRuler

class Ruler(object):

    @staticmethod
    def setV(source, batch={}):
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
        dsort = OrderedDict(sorted(batch.items(), key=lambda x: x[0]))
        return sha1(repr(dsort).encode('utf-8')).hexdigest()

    @staticmethod
    def batch(source, batch):
        items = source.items()
        return IteratorRuler().batch(items=items, Ruler=Ruler, source=batch).result()

    @staticmethod
    def fctTags(source, batch):
        tags = []
        dirts = Ruler.switch(source, batch, {})

        for key, item in dirts.items():
            clean = {
                'key': key,
                'value': item
            }
            tags.append(clean)
        return tags

    @staticmethod
    def now(source, batch):
        return datetime.datetime.now()

    @staticmethod
    def SyncForeignEntityByTag(source, batch):
        result = []

        tentity = Ruler.switch(source['field'], batch)
        if tentity:
            result += sync_apps(tentity, source['resource'])

        tentity = Ruler.switch("%s_id" % source['field'], batch)
        if tentity:
            result += sync_apps(tentity, source['resource'], '_id')

        return result
