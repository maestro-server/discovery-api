
from openstack import profile, connection

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
        prof = profile.Profile()
        prof.set_region(profile.Profile.ALL, self._region)

        conn = connection.Connection(
            profile=prof,
            auth_url=self._conn['url'],
            project_name=self._conn['project'],
            username=self._access['username'],
            password=self._access['password']
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
            output = getattr(self._client, resource)(details=True, **self._params)
            clear = []
            for server in output:
                obj = props(server)
                cc = omit(obj, ['_body', '_get_id', '_header', '_query_mapping', '_uri'])
                clear.append(cc)
                print("===========================3")
                if len(clear) >= limit:
                    self.setPag(server.id)
                    break
        except (HttpException, SDKException) as error:
            raise ClientMaestroError(error)

        return clear