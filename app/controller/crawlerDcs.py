
from flask_restful import Resource
from app.repository.adminer import Adminer


class CrawlerDcs(Resource):
    def get(self, datacenter):
        path = '.permissions.%s' % datacenter
        return Adminer().getOptions('connections', path)