from pydash.objects import get, merge_with, omit
from .merge.merge_rules import MergeRules


class MergeAPI(object):

    def __init__(self, content=None, key_comparer='name'):
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
            active = get(item, 'active', False)  # bugfix - if is false, update to true

            for key, find in enumerate(insert):

                if self.assign(find, dc_id):
                    check_insert = str(get(insert[key], 'checksum'))

                    if (active is False) or (check_insert != check_content) or 1 == 1:
                        created = omit(insert[key], self.omit)
                        merged = merge_with(item, created, MergeRules().merger_with)
                        santinize.append(merged)

                    if len(insert) <= 1:
                        insert = []
                    if len(insert) > 1:
                        del insert[key]
                    break

        return santinize + insert

    def assign(self, data, dc_id):
        return get(data, self.key) == dc_id
