

from flask_restful import Resource
from app.libs.appInfo import appInfo


class HomeApp(Resource):


    def get(self):
        """
        @api {get} / Ping
        @apiName GetPing
        @apiGroup Ping

        @apiSuccessExample {json} Success-Response:
        HTTP/1.1 201 OK
        {
           app: (String)
           description: (String)
           version: (String)
        }
        """
        return appInfo()