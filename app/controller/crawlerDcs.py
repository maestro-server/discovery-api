
import json, requests
from flask_restful import Resource
from app.libs.url import FactoryURL
from app.libs.lens import lens

class CrawlerDcs(Resource):
    """
    @api {get} /crawler/<datacenter> 4. Resources allowed by provider
    @apiName GetCrawlerDC
    @apiGroup Crawler

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "resource": (object) {
            "<api name>": (string)
        }
    }
    """
    def get(self, datacenter):
        path = FactoryURL.make(path="adminer")
        filters = json.dumps({'key': 'connections'})
        result = requests.post(path, json={'query': filters})

        if 'items' in result.json():
            return lens(result.json()['items'], len='.permissions.%s' % (datacenter))