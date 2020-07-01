import paramiko
import io
import json
from functools import reduce
from app.libs.logger import logger
from app.services.connector.connector import Connector


class AuthSSH(Connector):

    def credencials(self):
        private_key_file = io.StringIO()
        private_key_file.write(self._access.get('key'))
        private_key_file.seek(0)
        pkey = paramiko.RSAKey.from_private_key(private_key_file)

        self._client = paramiko.SSHClient()
        self._client.load_system_host_keys()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(hostname=self._access.get('host', 'localhost'),
                             port=self._access.get('port', 22),
                             username=self._access.get('user'),
                             pkey=pkey)
        return self

    def select(self, command):
        self.credencials()
        return self

    def getPag(self):
        return self._pagination

    def setPag(self, data):
        pass

    def exec_command(self, command):
        _, stdout, _ = self._client.exec_command(command)
        output = stdout.readlines()

        return output

    def make_result(self, path):
        if path:
            try:
                output = self.exec_command('cat %s' % path)

                mstring = reduce(lambda x,y:x+y, output)
                obj = json.loads(mstring)

                if self._path_result:
                    return obj.get(self._path_result)
                return obj
            except Exception as error:
                logger.error("MaestroAuthSSH: %s" % str(error))

    def execute(self):
        pass
