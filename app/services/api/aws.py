
import boto3
from .connector import Connector
from pydash.objects import get

from app.error.clientMaestroError import ClientMaestroError
from botocore.exceptions import ClientError

class AWS(Connector):

    def setNextToken(self, val):
        self.setParams('NextToken', val)
        return self

    def credencials(self, command):
        self._client = boto3.client(
            command,
            aws_access_key_id=self._access['access'],
            aws_secret_access_key=self._access['secret'],
            region_name=self._region
        )
        return self

    def select(self, command):
        self.credencials(command)
        return self

    def execute(self, resource):
        try:
            output = getattr(self._client, resource)(**self._params)
            return get(output, self._path_result)

        except ClientError as error:
            raise ClientMaestroError(error)