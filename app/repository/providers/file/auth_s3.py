from app.services.connector.auth_s3 import AuthS3
from app.error.clientMaestroError import ClientMaestroError
from botocore.exceptions import ClientError, ParamValidationError


class FileS3(AuthS3):

    def execute(self, resource):
        results = []

        try:
            path = self._access.get('path', '').strip("/")
            output = self._client.list_objects_v2(Bucket=self._access['bucket'], Prefix=path, **self._params)
            self.setPag(output)

            for key in output.get('Contents'):
                json = self.get_content(key['Key'])

                if json:
                    results = results + json

            return results

        except (ClientError, ParamValidationError) as error:
            raise ClientMaestroError(error)
