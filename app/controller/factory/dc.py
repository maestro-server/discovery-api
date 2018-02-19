
import os,json
from math import ceil
from flask import request
from flask_restful import Resource

from app.libs.deepUpdateForMongo import updaterIds
from app.services.filter import FilterAPI
from pydash import defaults, has, get, map_values_deep, omit
from app.error.missingError import MissingError

class DcApp(Resource):
    def get(self):
        req = request.args.to_dict()

        if not has(req, 'query'):
            return MissingError('id', 'Query params is needed'), 422

        if not has(req, 'query.roles._id'):
            return MissingError('id', 'Must have owner id'), 422

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


    def post(self):
        req = request.get_json(force=True)
        pagination = defaults(req, {'limit': os.environ.get("MAESTRO_SCAN_QTD", 200), 'page': 1})
        limit = int(pagination['limit'])
        page = int(pagination['page'])
        skip = (page - 1) * limit

        query = {}
        if has(req, 'query'):
            query = json.loads(req['query'])

        args = FilterAPI()\
            .addBatchFilters(query)\
            .make()

        count = self.entity().count(args)
        return {
            'found': count,
            'total_pages': ceil(count / limit) + 1,
            'page': page,
            'limit': limit,
            'items': self.entity().getAll(args, limit, skip)
        }

    def put(self):
        data = request.get_json(force=True)

        format = []

        for item in data['body']:
            id = get(item, '_id')
            id = self.entity().makeObjectId(id)

            item = omit(item, ['_id', 'updated_at'])
            item = map_values_deep(item, updaterIds)

            format.append({
                'filter': id,
                'data': item
            })
        return self.entity().batch_process(format)