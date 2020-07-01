from pydash.objects import defaults, get


class FilterAPI(object):

    def __init__(self):
        self.__filter = {}
        self.__default = {}

    def setDefault(self, default):
        self.__filter = defaults(self.__filter, default)
        return self

    def get(self, key):
        return get(self.__filter, key)

    def make(self):
        return self.__filter
