
from .model import Model
from pydash.objects import get

class Adminer(Model):

    def getOptions(self, filter, len = ''):
        list = self.col.find({'key': filter})
        if list:
            return get(list, '[0].value%s' % len)