from app.services.connector.auth_upload import AuthUpload
from app.error.clientMaestroError import ClientMaestroError


class AnsibleUpload(AuthUpload):

    def execute(self, resource):
        results = []
        try:
            for idx in self._client:
                results.append(self.make_result(idx))
            return results

        except Exception as error:
            raise ClientMaestroError(error)
