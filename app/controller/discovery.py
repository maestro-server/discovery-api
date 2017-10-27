
from flask_restful import Resource

class DiscoveryApp(Resource):
    def get(self):
        return {
            'name': 'Discovery API',
            'version': '0.10'
        }