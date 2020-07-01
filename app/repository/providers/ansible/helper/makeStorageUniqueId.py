import re
from pydash.objects import get


class makeStorageUniqueId(object):
    rules = ['extractAwsUuid', 'byLastLinkID', 'byPartitionUUID', 'byUUID', 'defaultValue']

    def __init__(self, key, value):
        self._key = key
        self._value = value

    def make(self):

        for fnc in makeStorageUniqueId.rules:
            data = getattr(self, fnc)()
            if data:
                return data

    def extractAwsUuid(self):
        ids = get(self._value, 'links.ids')
        for id in ids:
            uuid = re.search(r'(vol[a-zA-Z0-9]*)', id).group()
            if uuid:
                return uuid.replace('vol', 'vol-')

    def byLastLinkID(self):
        links = get(self._value, 'links.ids')
        lst = len(links) - 1
        return get(self._value, 'links.ids[%s]' % lst)

    def byUUID(self):
        return get(self._value, 'uuids[0]')

    def byPartitionUUID(self):
        ptns = self._value.get('partitions', {})
        for _, value in ptns.items():
            uuid = value.get('uuid')
            if uuid:
                return uuid

    def defaultValue(self):
        return '%s_%s' % (self._value.get('sectors'), self._key)
