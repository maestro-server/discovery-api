
import boto3
from .connector import Connector
from pydash.objects import get

from app.error.clientMaestroError import ClientMaestroError
from botocore.exceptions import ClientError

class AWS(Connector):
    __filter = []
    __instance_ids = []
    __max_result = 10
    __next_token = None
    __path_result = 'Reservations'

    def __init__(self, access, region):
        self.__access = access
        self.__region = region

    def setFilters(self, filters):
        self.__filter = filters

    def setInstanceIds(self, ids):
        self.__instance_ids = ids

    def setMaxResults(self, qtd):
        self.__max_result = qtd

    def setNextToken(self, token):
        self.__next_token = token


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
            output = getattr(self.__client, resource)(
                DryRun=True,
                Filters=self.__filter,
                InstanceIds=self.__instance_ids,
                MaxResults=self.__max_result
            )

            return get(output, self.__path_result)

        except ClientError as error:
            raise ClientMaestroError(error)