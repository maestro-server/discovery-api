
from flask_restful import Resource
from app.validate.connValidate import connValidate
from app.models import Providers

class ConnectionApp(Resource):
    def get(self, instance):
        return Providers(instance).get()

    def patch(self, instance):
        valid = connValidate().validate()

        if valid:
            Provider = Providers(instance)
            return Provider.markStatus(valid['status'], valid['task']).updateState(valid['msg'])

        return valid