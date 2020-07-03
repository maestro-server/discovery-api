from app.services.connector.connector import Connector
from app.repository.externalMaestroServer import ExternalMaestroServer
from app.libs.logger import logger

class AuthUpload(Connector):

    def credencials(self):
        self._client = self._access.get('artifacts', [])
        return self

    def select(self, command):
        self.credencials()
        return self

    def getPag(self):
        return self._pagination

    def setPag(self, data):
        pass

    def make_result(self, path):
        results = ExternalMaestroServer() \
            .list_request(path="users/upload/file?filename=%s" % path) \
            .get_results(self._path_result)

        logger.error(results)
        return results

    def execute(self):
        pass
