from pydash.utilities import identity
from pydash.objects import merge, pick_by


class MergeRulesDict(object):
    def dict_merge(self, list_obj, list_src):
        list_src = pick_by(list_src, identity)
        return merge(list_obj, list_src)
