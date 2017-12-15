
import boto3
from .connector import Connector
from pydash.objects import get
from botocore.client import Config

from app.error.clientMaestroError import ClientMaestroError
from botocore.exceptions import ClientError, ParamValidationError

class AWS(Connector):

    def setNextToken(self, val):
        self.setParams('NextToken', val)
        return self

    def credencials(self, command):
        config = Config(connect_timeout=10, read_timeout=10)

        self._client = boto3.client(
            command,
            aws_access_key_id=self._access['access'],
            aws_secret_access_key=self._access['secret'],
            region_name=self._region,
            config=config
        )
        return self

    def select(self, command):
        self.credencials(command)
        return self

    def setPag(self, data):
        token = get(data, 'NextToken')
        if token:
            self._pagination = {'NextToken': token}

    def getPag(self):
        return self._pagination

    def execute(self, resource):
        try:
            output = getattr(self._client, resource)(**self._params)
            self.setPag(output)
            return get(output, self._path_result)

        except (ClientError, ParamValidationError) as error:
            raise ClientMaestroError(error)