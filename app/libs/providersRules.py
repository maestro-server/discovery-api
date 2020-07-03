import os
import json
from app import app
from pydash import pick
from app.libs.logger import logger

def get_files(path, type):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '%s.json' % type in file:
                files.append(os.path.join(r, file))
    return files


def get_info(file):
    with open(file, 'r') as f:
        return json.load(f)


def providersRules(provider=""):
    files = file_extract('permission', provider)

    return data_extract(files, ["name"])


def providersInfo(provider=""):
    files = file_extract('info', provider)

    return {
        "providers": data_extract(sorted(files), ["icon", "label", "method"])
    }


def file_extract(name, provider):
    provider = provider.lower()
    root_path = os.path.join(app.root_path, '')
    path = '%srepository/providers/%s' % (root_path, provider)
    return get_files(path, name)


def data_extract(files, filter):
    if len(files) == 1:
        return get_info(files[0])

    extract = []
    for f in files:
        data = get_info(f)
        extract.append(pick(data, filter))

    return extract
