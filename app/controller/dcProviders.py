
from flask_restful import Resource
from app.repository import Providers

class DcProvidersApp(Resource):
    def get(self, id_conn):
        return Providers(id_conn).get()