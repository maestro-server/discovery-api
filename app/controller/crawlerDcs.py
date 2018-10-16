
import json
from flask_restful import Resource
from app.libs.lens import lens
from app.repository.externalMaestroData import ExternalMaestroData

class CrawlerDcs(Resource):
    # @api {get} /crawler/<datacenter> 4. Resources allowed by provider
    # @apiName GetCrawlerDC
    # @apiGroup Crawler

    # @apiSuccessExample {json} Success-Response:
    # HTTP/1.1 200 OK
    # {
    #     "resource": (object) {
    #         "<api name>": (string)
    #     }
    # }
    def get(self, datacenter):

        filters = json.dumps({'key': 'connections'})
        result = ExternalMaestroData()\
                    .post_request(path="adminer", body={'query': filters})\
                    .get_results('items')

        if result:
            return lens(result, len='.permissions.%s' % (datacenter))