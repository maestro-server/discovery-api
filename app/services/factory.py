
from pydash.objects import get
from app.services.api.aws import AWS
from app.services.api.openstack import OpenStack
from app.services.api.digitalocean import DigitalOcean
from app.services.api.s3 import S3

class FactoryAPI(object):

    able = {'AWS': AWS, 'OpenStack': OpenStack, 'Digital Ocean': DigitalOcean, 'Spaces (DO)': S3}

    def __init__(self, access, conn):
        self.access = access
        self.dc = get(conn, 'provider')
        self.srv = get(conn, 'service')
        self.region = self.translateRegion(get(conn, 'region'))
        self.conn = conn

        self.provider = None

    def translateRegion(self, data):
        return data.split(' ')[0]

    def execute(self, options, params = []):
        res = self.run(options=options, params=params)
        return {'cmd': options, 'region': self.region, 'result': res}

    def checkPag(self):
        if not self.provider:
            return None

        return self.provider.getPag()

    def isLast(self):
        return not self.provider.getPag()

    def run(self, options, params):

        provider = self.able[self.srv]
        self.provider = provider(access=self.access, region=self.region, conn=self.conn, opts=options.get('conf', {}))

        return self.provider\
            .setPathResult(options['result_path'])\
            .batchParams(params)\
            .select(options['command'])\
            .execute(options['access'])