
from flask_restful import Resource
from app.validate.connValidate import connValidate
from app.repository import Connections

class ConnectionApp(Resource):
    """
    @api {get} /connection/<instance> 1. Get single connection
    @apiName GetConnection
    @apiGroup Connection

    @apiParam {String} instance Instance ID of connection.

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    [{
        'name': (Number)
    }]
    """

    def get(self, instance):
        return Connections(instance).get()

    """
    @api {post} /connection/<instance> 2. Change connection state
    @apiName PostConnection
    @apiGroup Connection
    
    @apiParam (Query) {String} instance Instance ID of connection.
    @apiParam (Body x-www) {String} status Status [Sucess, warning, error]
    @apiParam (Body x-www) {String} task Specific task [server-list, dbs-list and etc]
    @apiParam (Body x-www) {String} msg Message

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    [{
        'name': (string),
        'status': (string) [sucess, warning or error]
        'task': (string)
    }]
    """

    def post(self, instance):
        valid = connValidate().validate()

        if valid:
            Connection = Connections(instance)
            return Connection.markStatus(valid['status'], valid['task']).updateState(valid['msg'])

        return valid