from .rules_dict import MergeRulesDict
from .rules_list import MergeRulesList
from .rules_list_storage import MergeRulesListStorage


class MergeRules(object):

    def __init__(self, rlist=MergeRulesList, rdict=MergeRulesDict, rcustom={'storage': MergeRulesListStorage}):
        self._ruler_list_default = rlist
        self._ruler_dict_default = rdict
        self._ruler_list_bag = rcustom

    def applyListRuler(self, key):
        return self._ruler_list_bag.get(key, self._ruler_list_default)

    def merger_with(self, obj_value, src_value, key, obj, source):
        if isinstance(obj_value, list) and isinstance(src_value, list):
            if len(obj_value) > 0 and len(src_value) > 0:
                Ruler = self.applyListRuler(key)
                return Ruler().list_merge(obj_value, src_value)

        if isinstance(obj_value, dict) and isinstance(src_value, dict):
            return self._ruler_dict_default().dict_merge(obj_value, src_value)
