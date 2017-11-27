
from flask_restful import Resource
from app.repository import Connections

class DcConnectionsApp(Resource):
    def get(self, id_conn):
        return Connections(id_conn).get()