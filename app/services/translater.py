
from app.services.api.aws import AWS
from app.services.api.openstack import OpenStack


class TranslateAPI(object):
    able = {'AWS': AWS, 'OpenStack': OpenStack}

    def __init__(self, provider, entity, limit):
        self.entity = entity
        self.provider = provider
        self.limit = limit

    def translate(self, result):
        x = 1
        i = 1
        total = len(result)

        while x <= total:
            x = (i * int(self.limit))
            i = i + 1
            print(i, x)
            yield result[1:100]

    def exec(self):
        provider = self.able[self.dc]
        return provider(self.entity, self.provider).translate()