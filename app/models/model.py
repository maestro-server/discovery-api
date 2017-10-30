
from app import db
from pydash.objects import get
from bson.objectid import ObjectId

class Model(object):

    def __init__(self):
        name = self.__class__.__name__.lower()
        self.col = db[name]

    def getAll(self, filter):
        list = self.col.find(filter)

    def get(self, id, len=''):
        list = self.col.find({'_id': ObjectId(id)})
        if list:
            return get(list, '[0]%s' % len)