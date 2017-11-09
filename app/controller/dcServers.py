
import os
from flask import request
from flask_restful import Resource
from app.models import Servers
from pydash.objects import defaults

class DcServersApp(Resource):
    def get(self, id_datacenter):
        req = request.args.to_dict()

        args = defaults(req, {'limit': os.environ.get("MAESTRO_TRANSLATE_QTD", 50), 'skip': 0})
        filter = {'datacenters._id': Servers.castObjectId(id_datacenter)}

        limit = int(args['limit'])
        skip = int(args['skip'])

        return {
            'found': Servers().count(filter),
            'limit': limit,
            'skip': skip,
            'items': Servers().getAll(filter, limit, skip)
        }

    def post(self, id_datacenter):
        req = request.args.to_dict()

        args = defaults(req, {'limit': os.environ.get("MAESTRO_TRANSLATE_QTD", 50), 'skip': 0})
        filter = {'datacenters._id': Servers.castObjectId(id_datacenter)}

        limit = int(args['limit'])
        skip = int(args['skip'])

        body = request.form.to_dict()

        print(body)

        return {
            'found': Servers().count(filter),
            'limit': limit,
            'skip': skip,
            'items': Servers().getAll(filter, limit, skip)
        }