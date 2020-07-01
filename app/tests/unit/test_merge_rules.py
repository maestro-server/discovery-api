import unittest
from app.services.merge.merge_rules import MergeRules
from app.services.merge.rules_list import MergeRulesList
from app.services.merge.rules_list_storage import MergeRulesListStorage


#
# MergeRules
#
class MergeRulesTests(unittest.TestCase):

    def test_merge_dict(self):
        obj_value = {'a': 'teste'}
        src_value = {'a': 'teste2'}
        key = 'myket'

        merged = MergeRules().merger_with(obj_value, src_value, key, {}, {})
        self.assertEqual(merged, src_value)

    def test_merge_list(self):
        obj_value = [{'a': 'teste'}]
        src_value = [{'a': 'teste2'}]
        key = 'myket'

        merged = MergeRules().merger_with(obj_value, src_value, key, {}, {})
        self.assertEqual(merged, obj_value + src_value)

    def test_merge_storage(self):
        obj_value = [{'a': 'teste'}]
        src_value = [{'a': 'teste2'}]
        key = 'storage'

        merged = MergeRules().merger_with(obj_value, src_value, key, {}, {})
        self.assertEqual(merged, src_value)


#
# MergeRulesList
#
class MergeRulesListTests(unittest.TestCase):

    def test_list_merge(self):
        arr1 = ['teste']
        arr2 = ['test2']

        arr = MergeRulesList().list_merge(arr1, arr2)
        self.assertEqual(arr, arr1 + arr2)

    def test_list_merge_obj(self):
        arr1 = [{'name': 'name1', 'spec': 'spec1'}]
        arr2 = [{'name': 'name2'}]
        arrR = [{'name': 'name1', 'spec': 'spec1'}, {'name': 'name2'}]

        arr = MergeRulesList().list_merge(arr1, arr2)
        self.assertEqual(arr, arrR)

    def test_empty(self):
        arr1 = []
        arr2 = []
        arrR = []

        arr = MergeRulesListStorage().list_merge(arr1, arr2)
        self.assertEqual(arr, arrR)


#
# MergeRulesListStorage
#
class MergeRulesListStorageTests(unittest.TestCase):

    def test_list_merge_obj(self):
        arr1 = [{'name': 'name1', 'spec': 'spec1', 'unique_id': 'a'}]
        arr2 = [{'name': 'name2', 'unique_id': 'a'}]
        arrR = [{'name': 'name2', 'spec': 'spec1', 'unique_id': 'a'}]

        arr = MergeRulesListStorage().list_merge(arr1, arr2)
        self.assertEqual(arr, arrR)

    def test_list_merge_obj2(self):
        arr1 = [{'name': 'name1', 'spec': 'spec1', 'unique_id': 'a'}, {'name': 'xxx', 'spec': 'xxx', 'unique_id': 'b'}]
        arr2 = [{'name': 'name2', 'unique_id': 'a'}]
        arrR = [{'name': 'name2', 'spec': 'spec1', 'unique_id': 'a'}]

        arr = MergeRulesListStorage().list_merge(arr1, arr2)
        self.assertEqual(arr, arrR)

    def test_empty(self):
        arr1 = []
        arr2 = []
        arrR = []

        arr = MergeRulesListStorage().list_merge(arr1, arr2)
        self.assertEqual(arr, arrR)


if __name__ == "__main__":
    unittest.main()
