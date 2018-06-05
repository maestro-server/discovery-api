
from openstack import connection

from .connector import Connector
from pydash.objects import get, omit

from app.error.clientMaestroError import ClientMaestroError
from openstack.exceptions import HttpException, SDKException

import inspect

def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not inspect.ismethod(value):
            pr[name] = value
    return pr

class OpenStack(Connector):

    def setNextToken(self, val):
        self.setParams('marker', val)
        return self

    def credencials(self, command):
        conn = connection.Connection(
            region_name=self._region,
            auth=dict(
                auth_url=self._conn['url'],
                username=self._access['username'],
                password=self._access['password'],
                project_id=self._conn['project'],
                user_domain_id=self._conn['user_domain_id']
            ),
            compute_api_version=self._conn['api_version']
        )

        try:
            conn.authorize()
            self._client = getattr(conn, command)
        except (HttpException, SDKException) as error:
            raise ClientMaestroError(error)

        return self

    def select(self, command):
        self.credencials(command)
        return self

    def setPag(self, data):
        if data:
            self._pagination = {'marker': data}

    def getPag(self):
        return self._pagination

    def execute(self, resource):

        try:
            limit = get(self._params, 'limit')
            output = getattr(self._client, resource)(**self._params)
            clear = []
            for server in output:
                obj = props(server)
                cc = omit(obj, ['_body', '_get_id', '_header', '_query_mapping', '_uri', 'detail_for'])
                clear.append(cc)

                if len(clear) >= limit:
                    self.setPag(server.id)
                    break
        except (HttpException, SDKException) as error:
            raise ClientMaestroError(error)

        return clear