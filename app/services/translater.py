
from app.services.translate.aws import MapperAWS


class TranslateAPI(object):
    able = {'AWS': MapperAWS}

    def __init__(self, provider, options, task, conn={}):
        self.task = task
        self.provider = self.able[provider](options['access'], conn)\
            .setResultPath(options['single_result_path'])

    def translate(self, data):
        result = []

        for item in data:
            tt = self.provider.translate(item)
            result.append(tt)

        return result