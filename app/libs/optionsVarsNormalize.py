import os, builtins
from pydash.objects import get


def optionsVarsNormalize(batch=[]):
    clear = []

    for item in batch:
        typ = get(item, 'type', str)
        default = get(item, 'default', None)

        val = os.environ.get(item['env'], default)
        typed = getattr(builtins, typ)(val)
        clear.append({item['name']: typed})

    return clear
