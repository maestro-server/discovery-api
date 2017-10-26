
from flask_restful import Resource

class DiscoveryApp(Resource):
    def get(self):
        return {'hello': 'world'}