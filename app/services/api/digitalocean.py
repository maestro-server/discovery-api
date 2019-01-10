
import re
from .polyform.digitalocean.manager import PolyManager
from .connector import Connector
from app.error.clientMaestroError import ClientMaestroError

class DigitalOcean(Connector):

    def credencials(self, command):

        self._client = PolyManager(
            token=self._access['token']
        )

        return self

    def select(self, command):
        self.credencials(command)
        return self

    def setPag(self, data):
        pages = data.get("links", {}).get("pages", {}).get("next")
        if pages:
            next = re.search(r'\?page=([0-9]*)', pages).group(1)
            self._pagination = {'page': next}

    def getPag(self):
        return self._pagination

    def execute(self, resource):
        try:
            output = getattr(self._client, resource)(**self._params)
            return output.get(self._path_result)

        except Exception as error:
            raise ClientMaestroError(error)