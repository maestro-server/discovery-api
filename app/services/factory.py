
from app.services.api.aws import AWS
from app.services.api.openstack import OpenStack
from pydash.objects import get

class FactoryAPI(object):

    def __init__(self, access, dc):
        self.access = access
        self.dc = dc
        self.regions = self.getRegions(access)

    def getRegions(self, data):
        rgs = get(data, 'regions', [])
        return list(map(lambda e: e.split(' ')[0], rgs))

    def execute(self, require):
        provider = globals()[self.dc]
        exec = provider(self.access, self.regions).execute(require)
        return exec