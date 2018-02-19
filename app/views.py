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

api.add_resource(DcConnectionsApp, '/connections')
api.add_resource(DcServersApp, '/servers')
api.add_resource(DcApplicationApp, '/applications')
api.add_resource(DcSystemApp, '/systems')
api.add_resource(DcVolumesApp, '/volumes')
api.add_resource(DcImagesApp, '/images')
api.add_resource(DcNetworkApp, '/networks')
api.add_resource(DcSnapshotsApp, '/snapshots')
api.add_resource(DcFlavorsApp, '/flavors')
api.add_resource(DcClientsApp, '/clients')
api.add_resource(DcServicesApp, '/services')
api.add_resource(DcProjectsApp, '/projects')
api.add_resource(DcTeamsApp, '/teams')
api.add_resource(DcEventsApp, '/events')
api.add_resource(DcDatacentersApp, '/datacenters')
api.add_resource(DcReportsApp, '/reports')
api.add_resource(AggregationApp, '/aggregate')

api.add_resource(CrawlerDcs, '/crawler/<datacenter>', '/crawler/<datacenter>/')
api.add_resource(CrawlerApps, '/crawler/<datacenter>/<instance>/<task>', '/crawler/<datacenter>/<instance>/<task>/')

@app.errorhandler(404)
def error(e):
    return jsonify({'error': 'Resource not found'}), 404