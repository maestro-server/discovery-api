# -*- encoding: utf-8 -*-
"""
Python Routes
Licence: GPLv3
"""

from flask_restful import Api
from app import app
from flask import jsonify

from .controller.discovery import DiscoveryApp
from .controller.crawler import CrawlerApp
from .controller.checker import CheckerApp

api = Api(app)

api.add_resource(DiscoveryApp, '/')
api.add_resource(CrawlerApp, '/crawler/<datacenter>')
api.add_resource(CheckerApp, '/crawler/<datacenter>/check')

@app.errorhandler(404)
def error(e):
    return jsonify({'error': 'Resource not found'})