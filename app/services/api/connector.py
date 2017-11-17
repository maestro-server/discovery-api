
from pydash.objects import merge
from abc import ABC, abstractmethod

class Connector(ABC):

    def __init__(self, access, region, conn):
        self._path_result = ''
        self._access = access
        self._region = region
        self._pagination = None
        self._conn = conn

        self._params = {}

    def setPathResult(self, data):
        self._path_result = data
        return self

    def setParams(self, key, val):
        self._params[key] = val
        return self

    def batchParams(self, batch = []):
        for item in batch:
            merge(self._params, item)
        return self

    @abstractmethod
    def credencials(self):
        pass

    @abstractmethod
    def setPag(self, data):
        pass

    @abstractmethod
    def getPag(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def execute(self):
        pass