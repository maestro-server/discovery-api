
from app import db
from pydash.objects import get
from bson.objectid import ObjectId
from app.error.missingError import MissingError

class Model(object):

    def __init__(self, id=None):
        name = self.__class__.__name__.lower()
        self.col = db[name]
        self.__id = id

    def getAll(self, filter):
        list = self.col.find(filter)

    def get(self, len=''):
        list = self.col.find(self.makeObjectId())
        if list:
            return get(list, '[0]%s' % len)

    def update(self, data):
        if not self.__id:
            raise MissingError('id', 'Id not setted')

        set = {'$set': data}
        result = self.col.update_one(self.makeObjectId(), set)
        return result.raw_result

    def makeObjectId(self):
        return {'_id': ObjectId(self.__id)}