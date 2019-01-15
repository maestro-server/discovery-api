from pydash import get
from app.services.translate import MapperAWS, MapperOpenStack, MapperDO, MapperSpaces, MapperAzure


class TranslateAPI(object):
    able = {
        'AWS': MapperAWS,
        'OpenStack': MapperOpenStack,
        'Digital Ocean': MapperDO,
        'Spaces (DO)': MapperSpaces,
        'Azure': MapperAzure
    }

    def __init__(self, provider, options, task, conn={}):
        self.task = task
        self.provider = self.able[provider](options['access'], conn) \
            .setResultPath(get(options, 'single_result_path', ''))

    def translate(self, data):
        result = []

        for item in data:
            tt = self.provider.translate(item)
            result.extend(tt)

        return result
