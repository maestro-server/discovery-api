
class IteratorTranslate(object):
    def __init__(self, limit):
        self.limit = int(limit)

    def batch(self, result):
        x = 1
        i = 1
        total = len(result)

        while (x + self.limit) <= (total + self.limit):
            x = (i * self.limit)
            pref = (x - self.limit)
            i += 1
            if len(result[pref:x]):
                yield result[pref:x]