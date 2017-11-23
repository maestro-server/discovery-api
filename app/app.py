# -*- encoding: utf-8 -*-
"""
Python Routes
Licence: GPLv3
"""

from flask_restful import Api
from app import app
from flask import jsonify

from .controller import *

api = Api(app)

api.add_resource(DiscoveryApp, '/')
api.add_resource(Crawler, '/crawler')
api.add_resource(ConnectionApp, '/connection/<instance>', '/connection/<instance>/')

api.add_resource(DcProvidersApp, '/providers/<id_conn>')
api.add_resource(DcServersApp, '/servers')
api.add_resource(DcApplicationApp, '/applications')

api.add_resource(CrawlerDcs, '/crawler/<datacenter>', '/crawler/<datacenter>/')
api.add_resource(CrawlerApps, '/crawler/<datacenter>/<instance>/<task>', '/crawler/<datacenter>/<instance>/<task>/')

@app.errorhandler(404)
def error(e):
    return jsonify({'error': 'Resource not found'})