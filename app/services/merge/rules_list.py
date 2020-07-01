from pydash.objects import has
from pydash.arrays import union_with
from pydash.predicates import is_equal


class MergeRulesList(object):
    def list_merge(self, list_obj, list_src):
        return union_with(list_obj, list_src, self.alg_equal)

    def alg_equal(self, src, new):
        if has(src, 'unique_id') and has(new, 'unique_id'):
            return is_equal(src['unique_id'], new['unique_id'])

        return is_equal(src, new)
