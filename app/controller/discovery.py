
import os, json
from pydash.objects import pick
from flask_restful import Resource

class DiscoveryApp(Resource):
    def get(self):
        fn = os.path.dirname(os.path.abspath(__file__))
        json_data = open(fn+'/../../package.json').read()
        data = json.loads(json_data)
        return pick(data, ['name', 'provider', 'description', 'version', 'license'])