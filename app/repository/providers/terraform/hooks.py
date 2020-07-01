from pydash.objects import get


class HookedTerraform(object):

    @staticmethod
    def fallbackVolumeName(obj, conn):
        unique = get(obj, 'unique_id')
        return get(obj, 'name', unique)
