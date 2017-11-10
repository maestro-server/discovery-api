
import os
import boto3
from .connector import Connector
from pydash.objects import get

from app.error.clientMaestroError import ClientMaestroError
from botocore.exceptions import ClientError

class AWS(Connector):

    def __init__(self, access, region):
        self.__access = access
        self.__region = region

        self.__params = {'MaxResults': int(os.environ.get("MAESTRO_SCAN_QTD", 100))}
        self.__path_result = 'Reservations'

    def setParams(self, key, val):
        self.__params[key] = val
        return self

    def setFilters(self, val):
        self.setParams('Filters', val)
        return self

    def setMaxResults(self, val):
        self.setParams('MaxResults', val)
        return self

    def setNextToken(self, val):
        self.setParams('NextToken', val)
        return self


    def credencials(self, command):
        self.__client = boto3.client(
            command,
            aws_access_key_id=self.__access['access'],
            aws_secret_access_key=self.__access['secret'],
            region_name=self.__region
        )
        return self

    def select(self, command):
        self.credencials(command)
        return self

    def execute(self, resource):
        try:
            output = getattr(self.__client, resource)(**self.__params)
            return get(output, self.__path_result)

        except ClientError as error:
            raise ClientMaestroError(error)