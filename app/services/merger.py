
from pydash.objects import get, merge, omit
from pydash.collections import find

class MergeAPI(object):

    def __init__(self, base = None):
        self.base = base
        self.inserted = []

    def merge(self, insert):
        if not isinstance(self.base, list):
            return insert

        for item in self.base:
            dc_id  = get(item, 'datacenters.instance_id')

            for key, find in enumerate(insert):
                if self.assign(find, dc_id):
                    created = omit(insert[key], ['created_at', 'roles', 'owner', 'status', 'active'])
                    insert[key] = merge({}, item, created)
                    break

        return insert

    def assign(self, data, dc_id):
        return get(data, 'datacenters.instance_id') == dc_id

