from .helpers.filter import filtering
from app.services.connector.auth_ssh import AuthSSH
from app.error.clientMaestroError import ClientMaestroError


class TerraformSSH(AuthSSH):

    def execute(self, resource):
        results = []
        try:
            output = self.exec_command('find %s -type f' % self._access.get('path'))

            for line in output:
                json = self.make_result(line)
                if json:

                    tf_filter = filtering(json, self._opts.get('filter'))
                    results = results + tf_filter

            return results

        except Exception as error:
            raise ClientMaestroError(error)
