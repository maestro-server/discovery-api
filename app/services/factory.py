
from app.services.api.aws import AWS
from app.services.api.openstack import OpenStack
from pydash.objects import get
from app.error.missingError import MissingError

class FactoryAPI(object):
    able = {'AWS': AWS, 'OpenStack': OpenStack}

    def __init__(self, access, dc):
        self.access = access
        self.dc = dc
        self.regions = self.getRegions(access)

        if not self.regions:
            raise MissingError(self.regions, 'Dont have any region in this connnection')

    def getRegions(self, data):
        rgs = get(data, 'regions', [])
        return list(map(lambda e: e.split(' ')[0], rgs))

    def execute(self, require):
        result = []

        for commands in require:
            for region in self.regions:
                res = self.exec(region, commands['access'], commands['command'])
                result.append({'cmd': commands, 'region': region, 'result': res})

        return result

    def exec(self, region, resource, command):
        provider = self.able[self.dc]
        return provider(self.access, region)\
            .select(command)\
            .execute(resource)