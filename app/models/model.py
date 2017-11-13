
import datetime
from app import db
from bson.objectid import ObjectId
from pymongo import InsertOne, UpdateOne
from app.error.missingError import MissingError

class Model(object):

    def __init__(self, id=None):
        name = self.__class__.__name__.lower()
        self.col = db[name]
        self.__id = id

    def getAll(self, filter = {}, limit = 10, skip = 0):
        result = self.col.find(filter)\
            .limit(limit)\
            .skip(skip)

        return list(result)

    def count(self, filter = {}):
        return self.col.count(filter)

    def get(self):
        return self.col.find_one(Model.makeObjectId(self.__id))

    def update(self, data):
        if not self.__id:
            raise MissingError('id', 'Id not setted')

        data = {**data, **self.makeUpdateAt()}
        set = {'$set': data}
        result = self.col.update_one(Model.makeObjectId(self.__id), set)
        return result.raw_result

    def batch_process(self, data):
        requests = []
        for item in data:
            obj = {**item['data'], **self.makeUpdateAt()}

            if item['filter']:
                cal = UpdateOne(item['filter'], {'$set': obj})
            else:
                cal = InsertOne(obj)

            requests.append(cal)

        result = self.col.bulk_write(requests)
        return result.bulk_api_result

    def makeUpdateAt(self):
        return {'updated_at': datetime.datetime.utcnow()}

    @staticmethod
    def makeObjectId(id):
        if id:
            return {'_id': Model.castObjectId(id)}

    @staticmethod
    def castObjectId(id):
        return ObjectId(id)