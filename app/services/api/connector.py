
import os, builtins
from abc import ABC, abstractmethod

class Connector(ABC):

    def __init__(self, access, region, conn = None):
        self._path_result = 'Reservations'
        self._access = access
        self._region = region
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
            typ = item['type']
            val = os.environ.get(item['env'], item['default'])
            typed = getattr(builtins, typ)(val)
            self.setParams(item['name'], typed)

        return self

    @abstractmethod
    def credencials(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def execute(self):
        pass