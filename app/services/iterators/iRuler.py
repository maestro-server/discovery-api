
from pydash.objects import pick_by, assign, get
from pydash.utilities import identity

class IteratorRuler(object):

    _translate = {}

    def __init__(self):
        self._translate = {}

    def push_data(self, data, single, merged = False):
        if merged is True:
            assign(self._translate, data)

        if merged is not True:
            self._translate[single] = data


    def batch(self, items, Ruler, source = {}):
        for key, item in items:
            res = getattr(Ruler, item['call'])(item['source'], source)

            if isinstance(res, dict):
                res = pick_by(res, identity)

            if not res == None:
                keys = key.split('|')

                for single in keys:
                    self.push_data(res, single, get(item, 'merged'))

        return self

    def result(self):
        return self._translate