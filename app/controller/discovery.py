
import os, json
from app import app
from pydash.objects import pick
from flask_restful import Resource

class DiscoveryApp(Resource):
    def get(self):
        root_path = os.path.join(app.root_path, '..')

        file = open(root_path+'/package.json')
        json_data = file.read()
        data = json.loads(json_data)

        file.close()
        return pick(data, ['name', 'provider', 'description', 'version', 'license'])