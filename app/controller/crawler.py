
from flask_restful import Resource

from app.services.privateAuth import private_auth


class Crawler(Resource):
    @private_auth
    def get(self):
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
        return {
            'resources':
                (
                    {"path": "/crawler/<datacenter>", "description": "List enabled datacenters"},
                    {"path": "/crawler/<datacenter>/<instance>/<task>/<type>",
                     "description": "Execute tasks, <instance> id connections instance, <tasks>: (server-list, dbs-list e etc),  <type>: (full, parcial or single)"}
                )
        }