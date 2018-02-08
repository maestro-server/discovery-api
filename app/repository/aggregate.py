
from app import db

class Aggregate(object):

    def __init__(self, name=None):
        self.col = db[name]

    def pipeline(self, pipeline):
        result = self.col.aggregate(pipeline)
        return list(result)