import re
from app.repository.providers.digitalocean.polyform.digitalocean.manager import PolyManager
from app.services.connector.connector import Connector
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
            cnext = re.search(r'\?page=([0-9]*)', pages).group(1)
            self._pagination = {'page': cnext}

    def getPag(self):
        return self._pagination

    def execute(self, resource):
        try:
            output = getattr(self._client, resource)(**self._params)
            return output.get(self._path_result)

        except Exception as error:
            raise ClientMaestroError(error)
