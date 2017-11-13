
import os

class FactoryURL(object):

    @staticmethod
    def make(path=""):
        base = os.environ.get("DISCOVERY_URL", "localhost")
        port = os.environ.get("PORT", "5000")

        return "http://%s:%s/%s" % (base, port, path)