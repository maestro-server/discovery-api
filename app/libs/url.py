
import os

class FactoryURL(object):

    @staticmethod
    def make(path=""):
        base = os.environ.get("MAESTRO_DISCOVERY_URL", "http://localhost")
        port = os.environ.get("MAESTRO_PORT", "5000")

        return "%s:%s/%s" % (base, port, path)