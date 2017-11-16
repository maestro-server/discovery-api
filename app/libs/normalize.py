
import os, builtins
from pydash.objects import get, set_

class Normalize(object):

    @staticmethod
    def optionsVarsNormalize(batch=[]):
        clear = []

        for item in batch:
            typ = get(item, 'type', str)
            default = get(item, 'default', None)

            val = os.environ.get(item['env'], default)
            typed = getattr(builtins, typ)(val)
            clear.append({item['name']: typed})

        return clear

    @staticmethod
    def singleKeyObjectIdToStr(data, key):
        set_(data, key, str(get(data, key)))

    @staticmethod
    def objectIdToStr(data):
        return str(data)