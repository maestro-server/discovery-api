import boto3
import json
from app.libs.logger import logger
from app.services.connector.connector import Connector
from pydash.objects import get
from botocore.client import Config


class AuthS3(Connector):

    def credencials(self, command):
        config = Config(connect_timeout=10, read_timeout=10)

        self._client = boto3.client(
            command,
            aws_access_key_id=self._access['access'],
            aws_secret_access_key=self._access['secret'],
            config=config
        )
        return self

    def select(self, command):
        self.credencials(command)
        return self

    def setPag(self, data):
        token = get(data, 'NextContinuationToken')

        if token:
            self._pagination = {'ContinuationToken': token}

    def getPag(self):
        return self._pagination

    def get_content(self, key):
        output = self._client.get_object(Bucket=self._access['bucket'], Key=key)

        try:
            content = output['Body'].read().decode('utf-8')
            obj = json.loads(content)
            if obj:
                if self._path_result:
                    return obj.get(self._path_result)
                return obj
        except Exception as error:
            logger.error("MaestroAuthS3: %s" % str(error))

    def execute(self):
        pass
