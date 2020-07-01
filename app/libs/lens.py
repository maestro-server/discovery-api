from pydash.objects import get


def lens(list, len=''):
    if list:
        return get(list, '[0].value%s' % len)
