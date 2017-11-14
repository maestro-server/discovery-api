
from app.services.api.aws import AWS
from app.services.api.openstack import OpenStack

class FactoryAPI(object):

    able = {'AWS': AWS, 'OpenStack': OpenStack}

    def __init__(self, access, dc, region):
        self.access = access
        self.dc = dc
        self.region = self.translateRegion(region)

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

    def run(self, options, params):
        provider = self.able[self.dc]
        self.provider = provider(self.access, self.region)

        return self.provider\
            .setPathResult(options['result_path'])\
            .batchParams(params)\
            .select(options['command'])\
            .execute(options['access'])