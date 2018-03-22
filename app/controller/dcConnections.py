
from app.controller.factory.dc import DcApp
from app.repository import Connections

import os,json
from math import ceil
from flask import request

from app.services.filter import FilterAPI
from pydash import defaults, has
from app.error.missingError import MissingError

class DcConnectionsApp(DcApp):
    """
    @api {get} /connections 1. Get all connections (GET)
    @apiName GetConnections
    @apiGroup Connections

    @apiParam {Object} query Filters.
    <br/>
    <pre class="prettyprint language-json" data-type="json">
    <code>{
    <br/>   "query": {
    <br/>       "roles": {
    <br/>           "_id": (String) // Must be
    <br/>       },
    <br/>       "limit": (Number)
    <br/>       "page": (Number)
    <br/>   }
    <br/>}
    <br/><br/>
    // You can use any field do filters
    <br/>{
    <br/>   "query": {
    <br/>       "roles": {
    <br/>           "_id": (String) // Must be
    <br/>       },
    <br/>       "_id": (String)
    <br/>       "name": (String)
    <br/>       "limit": (Number)
    <br/>       "page": (Number)
    <br/>   }
    <br/>}
    </code>
    </pre>

    query.roles._id Must be required.

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    [{
        'found': (Number),
        'total_pages': (Number),
        'page': (Number),
        'limit': (Number),
        'items': (Array)
    }]
    """

    """
    @api {post} /connections 2. Get all connections (POST)
    @apiName PostConnections
    @apiGroup Connections
    @apiDescription Look like te same of get action, if you need to do a long filters likes a list of ids, you can use this endpoint.

    @apiParam {Object} query Filters.
    <br/>
    <pre class="prettyprint language-json" data-type="json">
    <code>{
    <br/>   "query": {
    <br/>       "roles": {
    <br/>           "_id": (String) // Must be
    <br/>       },
    <br/>       "limit": (Number)
    <br/>       "page": (Number)
    <br/>   }
    <br/>}
    </code>
    </pre>

    query.roles._id Must be required.

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    [{
        'found': (Number),
        'total_pages': (Number),
        'page': (Number),
        'limit': (Number),
        'items': (Array)
    }]
    """

    """
    @api {put} /connections 3. Create or edit a list of entities
    @apiName PutConnections
    @apiGroup Connections
    @apiDescription Batch create or edit entities.

    @apiParam {Array} body List of batches data, if exist _id this item only be updated, otherwise will be created.

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    [{
        'filter': (Object),
        'data': (Array)
    }]
    """
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