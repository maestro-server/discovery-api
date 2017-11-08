
from app.services.translate.aws import MapperAWS


class TranslateAPI(object):
    able = {'AWS': MapperAWS}

    def __init__(self, provider, entity, task):
        self.task = task
        self.provider = self.able[provider](entity)

    def translate(self, data):
        result = []

        for item in data:
            tt = self.provider.translate(item)
            result.append(tt)

        return result