
import os,json
from flask import request
from flask_restful import Resource

from app.services.filter import FilterAPI
from app.models import Servers
from pydash.objects import defaults, has, get, map_values_deep, omit

from app.services.rules.ruler import Ruler


class DcServersApp(Resource):
    def get(self, id_datacenter = None):
        req = request.args.to_dict()
        pagination = defaults(req, {'limit': os.environ.get("MAESTRO_TRANSLATE_QTD", 50), 'skip': 0})
        limit = int(pagination['limit'])
        skip = int(pagination['skip'])

        query = {}
        if has(req, 'query'):
            query = json.loads(req['query'])

        args = FilterAPI()\
            .addFilters('datacenters._id', id_datacenter) \
            .addBatchFilters(query) \
            .make()

        return {
            'found': Servers().count(args),
            'limit': limit,
            'skip': skip,
            'items': Servers().getAll(args, limit, skip)
        }

    def put(self, id_datacenter = None):
        data = request.get_json(force=True)


        format = []
        for item in data['body']:
            id = get(item, '_id')
            id = Servers.makeObjectId(id)

            item = omit(item, ['_id', 'created_at', 'updated_at'])
            item = map_values_deep(item, self.updaterIds)

            format.append({
                'filter': id,
                'data': item
            })
        return Servers().batch_process(format)

    def updaterIds(self, data, path):
        last = path[-1]
        return Ruler.searchID(last, data)