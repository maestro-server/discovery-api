
from app.services.translate.aws import MapperAWS


class TranslateAPI(object):
    able = {'AWS': MapperAWS}

    def __init__(self, provider, entity, task, conn={}):
        self.task = task
        self.provider = self.able[provider](entity, conn)

    def translate(self, data):
        result = []

        for item in data:
            tt = self.provider.translate(item)
            result.append(tt)

        return result