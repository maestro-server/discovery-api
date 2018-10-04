
from abc import ABC, abstractmethod
from app.repository.externalMaestroData import ExternalMaestroData

class Mapper(ABC):

    def __init__(self, command, conn):
        self.command = command
        self.conn = {**conn, **self.getConnection(conn['id'])}
        self._result_path = ""

    def setResultPath(self, data):
        self._result_path = data
        return self

    def getConnection(self, id):
        content = ExternalMaestroData(id)\
                    .get_request(path="connections/%s" % id)\
                    .get_results()

        return content

    @abstractmethod
    def translate(self):
        pass