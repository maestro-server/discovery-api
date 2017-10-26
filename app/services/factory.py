
from app.services.api.aws import AWS
from app.services.api.openstack import OpenStack

class FactoryAPI(object):
    able = ['AWS', 'OpenStack']

    def __init__(self, access, dc):
        self.access = access
        self.dc = dc

    def check(self, require):
        if self.dc not in self.able:
            return {'error': 'DC not allowed'}

        provider = globals()[self.dc]
        check = provider(self.access).validate(require)

        return check