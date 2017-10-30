
from flask_restful import Resource

class Crawler(Resource):
    def get(self):
        return {
            'resources':
                (
                    {"path": "/crawler/<datacenter>", "description": "List enabled datacenters"},
                    {"path": "/crawler/<datacenter>/<instance>/<task>/<type>",
                     "description": "Execute tasks, <instance> id providers instance, <tasks>: (server-list, dbs-list e etc),  <type>: (full, parcial or single)"}
                )
        }