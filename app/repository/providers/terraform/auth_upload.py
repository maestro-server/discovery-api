from .helpers.filter import filtering
from app.services.connector.auth_upload import AuthUpload
from app.error.clientMaestroError import ClientMaestroError


class TerraformUpload(AuthUpload):

    def execute(self, resource):
        results = []
        try:
            for idx in self._client:
                tf_filter = filtering(self.make_result(idx), self._opts.get('filter'))
                results = results + tf_filter

            return results

        except Exception as error:
            raise ClientMaestroError(error)
