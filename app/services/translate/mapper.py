
import requests
from abc import ABC, abstractmethod
from app.libs.url import FactoryURL

class Mapper(ABC):

    def __init__(self, command, conn):
        self.command = command
        self.conn = {**conn, **self.getProvider(conn['id'])}

    def getProvider(self, id):
        path = FactoryURL.make(path="providers/%s" % id)
        resource = requests.get(path)
        content = resource.json()
        return content

    @abstractmethod
    def translate(self):
        pass