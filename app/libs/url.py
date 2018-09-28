
import os

class FactoryURL(object):

    @staticmethod
    def make(path=""):
        base = os.environ.get("MAESTRO_DATA_URI", "http://localhost:5010")

        return "%s/%s" % (base, path)