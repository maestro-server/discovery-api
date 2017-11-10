
import os, json
from flask import request
from flask_restful import Resource

from app.services.filter import FilterAPI
from app.models import Servers
from pydash.objects import defaults


class DcServersApp(Resource):
    def get(self, id_datacenter):
        req = request.args.to_dict()
        pagination = defaults(req, {'limit': os.environ.get("MAESTRO_TRANSLATE_QTD", 50), 'skip': 0})
        limit = int(pagination['limit'])
        skip = int(pagination['skip'])

        args = FilterAPI()\
            .addFilters('datacenters._id', id_datacenter)\
            .make()

        return {
            'found': Servers().count(args),
            'limit': limit,
            'skip': skip,
            'items': Servers().getAll(args, limit, skip)
        }

    def post(self, id_datacenter):
        req = request.args.to_dict()
        pagination = defaults(req, {'limit': os.environ.get("MAESTRO_TRANSLATE_QTD", 50), 'skip': 0})
        limit = int(pagination['limit'])
        skip = int(pagination['skip'])

        req = request.get_json(force=True)
        args = FilterAPI() \
            .addBatchFilters(request.get_json(force=True)) \
            .make()

        return {
            'args': args,
            'found': Servers().count(args),
            'limit': limit,
            'skip': skip,
            'items': Servers().getAll(args, limit, skip)
        }