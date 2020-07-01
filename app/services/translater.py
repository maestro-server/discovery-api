from pydash.objects import get
from app.repository.providers.translateIndex import TranslateIndex


class TranslateAPI(object):
    able = TranslateIndex.translators()

    def __init__(self, provider, options, task, conn={}):
        self.task = task
        self.opt = options
        self.provider = self.able[provider](options, conn) \
            .setResultPath(self.opt.get('single_result_path', ''))

    def translate(self, data):
        result = []

        for item in data:
            hook = self.opt.get('single_translate_hook', {})
            item = TranslateHook(hook.get('opts')).apply(item, hook.get('hook'))
            translated = {}


            if isinstance(item, list):
                translated = self.iterList(item)

            if isinstance(item, dict):
                translated = self.provider.translate(item)

            result.extend(translated)

        return result

    def iterList(self, items):
        narr = []
        for item in items:
            translated = self.provider.translate(item)
            narr.extend(translated)

        return narr


class TranslateHook(object):

    def __init__(self, opts):
        self._opts = opts

    def apply(self, obj, attr=None):
        if attr and hasattr(self, attr):
            return getattr(self, attr)(obj)

        return self.singleObj(obj)

    def singleObj(self, obj):
        return obj

    def mapReduceOnList(self, obj):
        narr = []
        fields = get(self._opts, 'field')

        for field in fields:
            garr = get(obj, field, [])
            narr.extend(garr)

        return narr

    def mapReduceOnDict(self, obj):
        narr = []
        fields = get(self._opts, 'field')

        for field in fields:
            items = get(obj, field, {})

            for key, item in items.items():
                item['_key'] = key
                narr.append(item)

        return narr
