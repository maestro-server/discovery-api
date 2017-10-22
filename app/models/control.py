

class Control(object):

    def __init__(self, dc):
        self.dc = dc

    def full(self):
        return "full %s" % self.dc

    def parcial(self, date):
        return "parcial %s %s" % (self.dc, date)

    def single(self, id_instance):
        return "single %s" % id_instance