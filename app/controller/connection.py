
from flask_restful import Resource
from app.validate.connValidate import connValidate
from app.repository import Connections

class ConnectionApp(Resource):
    def get(self, instance):
        return Connections(instance).get()

    def post(self, instance):
        valid = connValidate().validate()

        if valid:
            Connection = Connections(instance)
            return Connection.markStatus(valid['status'], valid['task']).updateState(valid['msg'])

        return valid