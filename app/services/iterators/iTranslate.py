
from app.views import app
import math

class IteratorTranslate(object):
    def __init__(self, result):
        self.limit = app.config['MAESTRO_TRANSLATE_QTD']
        self.result = result
        self.total = len(result)
        self.page = math.ceil(self.total/self.limit)
        self.iter = 1

    def isLast(self):
        return self.iter > self.page

    def batch(self):
        x = 1

        while (x + self.limit) <= (self.total + self.limit):
            x = (self.iter * self.limit)
            pref = (x - self.limit)
            self.iter += 1

            if len(self.result[pref:x]):
                yield self.result[pref:x]