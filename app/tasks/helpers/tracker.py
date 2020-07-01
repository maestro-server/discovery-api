
class HelperQueryTracker(object):

    def __init__(self):
        self._field = ""
        self._query = ""

    def make_tracker(self, dc_id, value):

        return [{
            '_id': dc_id,
            self._query: {
                self._field: value
            }
        }]

    def query(self, query):
        self._query = query
        return self

    def tracker(self, task, accountant, region):
        self._field = "tracker.%s.%s.%s" % (task, accountant, region)
        return self