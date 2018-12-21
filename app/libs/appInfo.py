
import os
import json
from app import app
from pydash import pick


def appInfo():
    root_path = os.path.join(app.root_path, '..')
    file = open(root_path + '/package.json')
    json_data = file.read()
    data = json.loads(json_data)

    file.close()
    return pick(data, ['name', 'provider', 'description', 'version', 'license'])