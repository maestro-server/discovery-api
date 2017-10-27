
from .model import Model
from pydash.arrays import head
from pydash.objects import get

class Adminer(Model):

    def getOptions(self, filter, path = ''):
        list = self.col.find({'key': filter})
        opts = head(list)
        return get(opts, 'value%s' % path)