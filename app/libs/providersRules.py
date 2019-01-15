
import os
import json
from app import app


def providersRules(action):
    root_path = os.path.join(app.root_path, '..')
    file = open(root_path + '/app/services/template/' + action + '.json')
    json_data = file.read()
    data = json.loads(json_data)

    file.close()
    return data