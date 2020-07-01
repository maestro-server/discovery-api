from pydash.objects import get


class HookedAnsible(object):

    @staticmethod
    def fallbackName(obj, conn):
        hostname = get(obj, 'hostname')
        return get(obj, 'name', hostname)
