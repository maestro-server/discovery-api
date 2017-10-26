
from flask_restful import Resource

class CrawlerApp(Resource):
    def get(self):
        return {'hello': 'world'}