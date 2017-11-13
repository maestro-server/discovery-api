
from pydash.arrays import union
from pydash.objects import get, merge, merge_with, omit, pick_by
from pydash.utilities import identity

class MergeAPI(object):

    def __init__(self, base = None):
        self.base = base
        self.inserted = []

    def merge(self, insert):
        if not isinstance(self.base, list):
            return insert

        for item in self.base:
            dc_id = get(item, 'datacenters.instance_id')

            for key, find in enumerate(insert):
                if self.assign(find, dc_id):
                    created = omit(insert[key], ['created_at', 'roles', 'owner'])
                    insert[key] = merge_with(item, created, MergeAPI.merger_with)
                    break

        return insert

    def assign(self, data, dc_id):
        return get(data, 'datacenters.instance_id') == dc_id

    @staticmethod
    def merger_with(obj_value, src_value, key, obj, source):
        if isinstance(obj_value, list) and isinstance(src_value, list):
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