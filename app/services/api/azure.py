import itertools
from .connector import Connector

from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from app.error.clientMaestroError import ClientMaestroError

from azure.common.exceptions import AuthenticationError

class Azure(Connector):

    _exec = {'compute': ComputeManagementClient, 'network': NetworkManagementClient}

    def credencials(self, command):

        try:
            credencials = ServicePrincipalCredentials(
                client_id=self._access['client'],
                secret=self._access['secret'],
                tenant=self._access['tenant']
            )

            cls = self._exec[command]
            self._client = cls(credencials, self._access['sub'])

        except AuthenticationError as error:
            raise ClientMaestroError(error)

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
        counter = 0

        while True:
            chunk_it = itertools.islice(it, n)
            try:
                first_el = next(chunk_it)
                counter += 1
            except StopIteration:
                if counter == 0:
                    raise ValueError('Empty result')
                return

            yield itertools.chain((first_el,), chunk_it)

    def handle_per_page(self):
        page = self._params.get('per_page', 50)

        if 'per_page' in self._params:
            del self._params['per_page']

        return page

    def execute(self, resource):
        executor = self._opts.get('exec', 'list_all')
        page = self.handle_per_page()

        try:
            client = getattr(self._client, resource)
            output = getattr(client, executor)(**self._params)

            if hasattr(output, '__iter__'):
                return self.grouper_it(page, output) #simulate a pagination with interator

            return output

        except Exception as error:
            raise ClientMaestroError(error)