
from flask_restful import Resource
from app.validate.connValidate import connValidate
from app.repository import Providers

class ConnectionApp(Resource):
    def get(self, instance):
        return Providers(instance).get()

    def post(self, instance):
        valid = connValidate().validate()

        if valid:
            Provider = Providers(instance)
            return Provider.markStatus(valid['status'], valid['task']).updateState(valid['msg'])

        return valid