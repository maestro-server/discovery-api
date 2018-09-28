
import json, requests
from flask_restful import Resource
from app.libs.url import FactoryURL
from app.libs.lens import lens
from app.libs.logger import logger

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
        path = FactoryURL.make(path="adminer")
        filters = json.dumps({'key': 'connections'})
        
        try:
            result = requests.post(path, json={'query': filters})
        except requests.exceptions.RequestException as error:
            logger.error("Discovery: Error - %s", str(error))

        if result and 'items' in result.json():
            return lens(result.json()['items'], len='.permissions.%s' % (datacenter))