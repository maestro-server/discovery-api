import itertools
from .connector import Connector

from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from app.error.clientMaestroError import ClientMaestroError

class Azure(Connector):

    _exec = {'compute': ComputeManagementClient, 'network': NetworkManagementClient}

    def credencials(self, command):

        credencials = ServicePrincipalCredentials(
            client_id=self._access['client'],
            secret=self._access['secret'],
            tenant=self._access['tenant']
        )

        cls = self._exec[command]
        self._client = cls(credencials, self._access['sub'])
        return self

    def select(self, command):
        self.credencials(command)
        return self

    def getPag(self):
        return self._pagination

    def setPag(self, data):
        pass


    def grouper_it(self, n, iterable):
        it = iter(iterable)
        while True:
            chunk_it = itertools.islice(it, n)
            try:
                first_el = next(chunk_it)
            except StopIteration:
                return

            yield itertools.chain((first_el,), chunk_it)

    def execute(self, resource):
        executor = self._opts.get('exec', 'list_all')

        try:
            client = getattr(self._client, resource)
            output = getattr(client, executor)(**self._params)

            return self.grouper_it(self._params.get('per_page'), output) #simulate a pagination with interator

        except Exception as error:
            raise ClientMaestroError(error)