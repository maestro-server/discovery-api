# -*- encoding: utf-8 -*-
"""
Python Routes
Licence: GPLv3
"""

from flask_restful import Api
from app import app
from flask import jsonify

from .controller import DiscoveryApp, Crawler, ConnectionApp, DcServersApp, CrawlerDcs, CrawlerApps

api = Api(app)

api.add_resource(DiscoveryApp, '/')
api.add_resource(Crawler, '/crawler')
api.add_resource(ConnectionApp, '/connection/<instance>', '/connection/<instance>/')
api.add_resource(DcServersApp, '/datacenters/<id_datacenter>/servers')

api.add_resource(CrawlerDcs, '/crawler/<datacenter>', '/crawler/<datacenter>/')
api.add_resource(CrawlerApps,
                 '/crawler/<datacenter>/<instance>/<task>',
                 '/crawler/<datacenter>/<instance>/<task>/',
                 '/crawler/<datacenter>/<instance>/<task>/<type>',
                 '/crawler/<datacenter>/<instance>/<task>/<type>/')

@app.errorhandler(404)
def error(e):
    return jsonify({'error': 'Resource not found'})