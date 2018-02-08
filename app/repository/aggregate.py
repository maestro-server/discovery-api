
from app import db

class Model(object):

    def __init__(self, id=None):
        self.col = db[name]
        self.__id = id

    def pipeline(self, pipeline):
        result = db.aggregate(pipeline)

        return list(result)