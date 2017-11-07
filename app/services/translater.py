
from app.services.api.aws import AWS
from app.services.api.openstack import OpenStack


class TranslateAPI(object):
    able = {'AWS': AWS, 'OpenStack': OpenStack}

    def __init__(self, provider, entity, limit):
        self.entity = entity
        self.provider = provider
        self.limit = limit

    def translate(self, result):
        i = 0
        total = len(result)

        while x <= total:
            x = i * self.limit
            yield result[x:self.limit]

    def exec(self):
        provider = self.able[self.dc]
        return provider(self.entity, self.provider).translate()