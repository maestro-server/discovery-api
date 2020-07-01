from pydash.objects import merge


class MergeRulesListStorage(object):
    def list_merge(self, list_obj, list_src):
        newarr = []

        for item in list_src:
            unique_id = item.get('unique_id')
            if unique_id:
                fitem = self.get_item_by_uniqueid(unique_id, list_obj)
                item = merge(fitem, item)

            newarr.append(item)

        return newarr

    def get_item_by_uniqueid(self, unique_id, arr):
        for item in arr:
            if unique_id == item.get('unique_id'):
                return item
