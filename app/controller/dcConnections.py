
from app.controller.factory.dc import DcApp
from app.repository import Connections

import os,json
from math import ceil
from flask import request

from app.services.filter import FilterAPI
from pydash import defaults, has
from app.error.missingError import MissingError

class DcConnectionsApp(DcApp):
    def __init__(self):
        self.entity = Connections

    def get(self):
        req = request.args.to_dict()

        if not has(req, 'query'):
            return MissingError('id', 'Query params is needed'), 422

        pagination = defaults(req, {'limit': os.environ.get("MAESTRO_SCAN_QTD", 200), 'page': 1})
        limit = int(pagination['limit'])
        page = int(pagination['page'])
        skip = (page-1) * limit

        query = json.loads(req['query'])

        args = FilterAPI() \
            .addBatchFilters(query) \
            .make()

        count = self.entity().count(args)
        return {
            'found': self.entity().count(args),
            'total_pages': ceil(count / limit),
            'page': page,
            'limit': limit,
            'items': self.entity().getAll(args, limit, skip)
        }