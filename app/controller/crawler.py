
from flask_restful import Resource

class Crawler(Resource):
    def get(self):
        return {
            'resources':
                (
                    {"path": "/crawler/<datacenter>", "description": "List enabled datacenters"},
                    {"path": "/crawler/<datacenter>/<type>/<instance>/<task>",
                     "description": "Execute tasks, <type>: (full, parcial or single), <instance> id providers instance, <tasks>: (server-list, dbs-list e etc)"}
                )
        }