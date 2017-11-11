

from flask_restful import Resource
from app.models import Servers

class DcServerSingleApp(Resource):
    def get(self, id_datacenter, id_server):
        return {
            'items': Servers(id_server).get()
        }