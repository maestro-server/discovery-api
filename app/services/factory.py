
from app.services.api.aws import AWS
from app.services.api.openstack import OpenStack

class FactoryAPI(object):

    able = {'AWS': AWS, 'OpenStack': OpenStack}

    def __init__(self, access, dc, region, options = {}):
        self.access = access
        self.dc = dc
        self.options = options
        self.region = self.translateRegion(region)

    def translateRegion(self, data):
        return data.split(' ')[0]

    def execute(self, commands):
        res = self.exec(self.region, commands['access'], commands['command'])
        return {'cmd': commands, 'region': self.region, 'result': res}

    def exec(self, region, resource, command):
        provider = self.able[self.dc]
        return provider(self.access, region)\
            .select(command)\
            .execute(resource)