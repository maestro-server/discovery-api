
from flask_restful import Resource

class CrawlerApps(Resource):
    def get(self, datacenter, type, instance, task):
        return {
            'datacenter': datacenter,
            'type': type,
            'instance': instance,
            'task': task
        }

    def put(self, datacenter, type, instance, task):
        pass