
from pydash.objects import defaults, get, merge
from app.services.rules.ruler import Ruler

class FilterAPI(object):

    def __init__(self):
        self.__filter = {}
        self.__default = {}

    def setDefault(self, default):
        self.__filter = defaults(self.__filter, default)
        return self

    def addFilters(self, key, rule):
        rule = Ruler.searchID(key, rule)
        rule = Ruler.translateLists(key, rule)
        rule = Ruler.searchAt(key, rule)

        obj = {key: rule}
        self.__filter = merge(self.__filter, obj)

        return self

    def addBatchFilters(self, arr):
        for key, item in arr.items():
           self.addFilters(key, item)

        return self

    def get(self, key):
        return get(self.__filter, key)

    def make(self):
        return self.__filter