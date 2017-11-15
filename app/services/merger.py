
from pydash.arrays import union
from pydash.objects import get, merge, merge_with, omit, pick_by
from pydash.utilities import identity

class MergeAPI(object):

    def __init__(self, content = None, key_comparer = 'name'):
        self.content = content
        self.inserted = []
        self.key = key_comparer
        self.omit = ['roles', 'owner']

    def merge(self, insert):
        if not isinstance(self.content, list):
            return insert

        for item in self.content:
            dc_id = get(item, self.key)

            for key, find in enumerate(insert):
                if self.assign(find, dc_id):
                    created = omit(insert[key], self.omit)
                    insert[key] = merge_with(item, created, MergeAPI.merger_with)
                    break

        return insert

    def assign(self, data, dc_id):
        return get(data, self.key) == dc_id

    @staticmethod
    def merger_with(obj_value, src_value, key, obj, source):
        if isinstance(obj_value, list) and isinstance(src_value, list):
            if len(obj_value) > 0 and len(src_value) > 0:
                return MergeAPI.list_merge(obj_value, src_value)

        if isinstance(obj_value, dict) and isinstance(src_value, dict):
            return MergeAPI.dict_merge(obj_value, src_value)


    @staticmethod
    def list_merge(list_obj, list_src):
        return union(list_obj, list_src)

    @staticmethod
    def dict_merge(list_obj, list_src):
        list_src = pick_by(list_src, identity)
        return merge(list_obj, list_src)