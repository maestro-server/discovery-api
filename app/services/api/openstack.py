
from openstack import profile, connection

from .connector import Connector
from pydash.objects import get

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
        except (HttpException, SDKException) as error:
            raise ClientMaestroError(error)

        self._client = getattr(conn, command)
        return self

    def select(self, command):
        self.credencials(command)
        return self

    def setPag(self, data):
        token = get(data, 'marker')
        if token:
            self._pagination = {'marker': token}

    def getPag(self):
        return self._pagination

    def execute(self, resource):
        print(self._params)
        output = getattr(self._client, resource)(details=True, limit=100, marker='616a62bd-45b7-4611-9cdb-37b6df676020')
        self.setPag(output)

        for server in output:
            print(props(server))


        return