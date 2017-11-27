
import requests
from abc import ABC, abstractmethod
from app.libs.url import FactoryURL

class Mapper(ABC):

    def __init__(self, command, conn):
        self.command = command
        self.conn = {**conn, **self.getConnection(conn['id'])}
        self._result_path = ""

    def setResultPath(self, data):
        self._result_path = data
        return self

    def getConnection(self, id):
        path = FactoryURL.make(path="connections/%s" % id)
        resource = requests.get(path)
        content = resource.json()
        return content

    @abstractmethod
    def translate(self):
        pass