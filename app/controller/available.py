
from app.libs.providersRules import providersRules
from flask_restful import Resource

from app.services.privateAuth import private_auth


class Available(Resource):
    @private_auth
    def get(self, action):
        """
        @api {get} /available/<action> 1. Available template connections
        @apiName GetAvailCrawler
        @apiGroup Available

        @apiParam (Param) {String} [action] Can be info or rules.

        @apiPermission JWT Private (MAESTRO_SECRETJWT_PRIVATE)
        @apiHeader (Header) {String} Authorization JWT {Token}

        @apiError (Error) PermissionError Token don`t have permission
        @apiError (Error) Unauthorized Invalid Token

        @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "resources": []
        }
        """
        if action in ['info', 'rules']:
            data = providersRules(action)
            return {
                "items": [
                    {"value": data}
                ]
            }