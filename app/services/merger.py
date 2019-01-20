
from pydash.arrays import union_with
from pydash.predicates import is_equal
from pydash.objects import has, get, merge, merge_with, omit, pick_by
from pydash.utilities import identity

class MergeAPI(object):

    def __init__(self, content = None, key_comparer='name'):
        self.content = content
        self.inserted = []
        self.key = key_comparer
        self.omit = ['roles', 'owner']

    def merge(self, insert):
        if not isinstance(self.content, list) or len(self.content) <= 0:
            return insert

        santinize = []
        for item in self.content:
            dc_id = get(item, self.key)
            check_content = str(get(item, 'checksum'))
            active = get(item, 'active', False) #bugfix - if is false, update to true

            for key, find in enumerate(insert):

                if self.assign(find, dc_id):
                    check_insert = str(get(insert[key], 'checksum'))

                    if (active is False) or (check_insert != check_content):
                        created = omit(insert[key], self.omit)
                        merged = merge_with(item, created, MergeAPI.merger_with)
                        santinize.append(merged)

                    if len(insert) <= 1:
                        insert = []
                    if len(insert) > 1:
                        del insert[key]
                    break

        return santinize + insert

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
        return union_with(list_obj, list_src, MergeAPI.algEqual)

    @staticmethod
    def algEqual(src, other):
        if has(src, 'unique_id') and has(other, 'unique_id'):
            return is_equal(src['unique_id'], other['unique_id'])

        return is_equal(src, other)


    @staticmethod
    def dict_merge(list_obj, list_src):
        list_src = pick_by(list_src, identity)
        return merge(list_obj, list_src)