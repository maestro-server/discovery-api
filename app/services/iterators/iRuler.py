
from pydash.objects import pick_by
from pydash.utilities import identity

class IteratorRuler(object):

    def batch(self, items, Ruler, source = {}):
        translate = {}
        for key, item in items:
            res = getattr(Ruler, item['call'])(item['source'], source)

            if isinstance(res, dict):
                res = pick_by(res, identity)

            if not res == None:
                translate[key] = res

        return translate