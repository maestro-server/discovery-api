
from flask_restful import Resource
from app.repository.adminer import Adminer


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
        path = '.permissions.%s' % datacenter
        return Adminer().getOptions('connections', path)