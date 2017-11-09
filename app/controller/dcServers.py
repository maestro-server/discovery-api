
from flask_restful import Resource
from app.models import Servers

class DcServersApp(Resource):
    def get(self, id_datacenter):
        return Servers().get()