
from app import db

class Model(object):

    def __init__(self):
        name = self.__class__.__name__.lower()
        self.col = db[name]