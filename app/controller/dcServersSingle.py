

from flask_restful import Resource
from app.models import Servers

class DcServerSingleApp(Resource):
    def get(self, id_datacenter, id_server):
        return {
            'items': Servers(id_server).get()
        }

    def put(self, id_datacenter, id_server):

        return {
            'id_datacenter': id_datacenter,
            'id_server': id_server
        }