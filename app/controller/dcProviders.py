
from flask_restful import Resource
from app.models import Providers

class DcProvidersApp(Resource):
    def get(self, id_conn):
        return Providers(id_conn).get()