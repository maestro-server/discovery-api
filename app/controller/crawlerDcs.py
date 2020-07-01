from flask_restful import Resource
from app.libs.providersRules import providersRules
from app.services.privateAuth import private_auth


class CrawlerDcs(Resource):
    @private_auth
    def get(self, datacenter):
        """
        @api {get} /crawler/<datacenter> 4. Resources allowed by provider
        @apiName GetCrawlerDC
        @apiGroup Crawler

        @apiPermission JWT Private (MAESTRO_SECRETJWT_PRIVATE)
        @apiHeader (Header) {String} Authorization JWT {Token}

        @apiError (Error) PermissionError Token don`t have permission
        @apiError (Error) Unauthorized Invalid Token

        @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "resource": (object) {
                "<api name>": (string)
            }
        }
        """
        result = providersRules(datacenter).get('permissions', {})
        if result:
            return result
