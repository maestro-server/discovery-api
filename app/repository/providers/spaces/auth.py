import boto3
from botocore.client import Config
from app.repository.providers.aws.auth import AWS


class S3(AWS):

    def credencials(self, command):
        config = Config(connect_timeout=10, read_timeout=10)

        self._client = boto3.client(
            command,
            aws_access_key_id=self._access['access'],
            aws_secret_access_key=self._access['secret'],
            endpoint_url="https://{}.digitaloceanspaces.com".format(self._region),
            region_name=self._region,
            config=config
        )
        return self
