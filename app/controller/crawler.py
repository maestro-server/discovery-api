
from flask_restful import Resource

class Crawler(Resource):
    """
    @api {get} /crawler/ 3. Endpoints allowed
    @apiName GetCrawler
    @apiGroup Crawler

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "resources": {
            "path": (string)
        }
    }
    """

    def get(self):
        return {
            'resources':
                (
                    {"path": "/crawler/<datacenter>", "description": "List enabled datacenters"},
                    {"path": "/crawler/<datacenter>/<instance>/<task>/<type>",
                     "description": "Execute tasks, <instance> id connections instance, <tasks>: (server-list, dbs-list e etc),  <type>: (full, parcial or single)"}
                )
        }