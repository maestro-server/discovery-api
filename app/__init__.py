# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from .celery import make_celery

app = Flask(__name__)
app.config.from_object('instance.config.Config')
app.config.from_object('app.services.privateAuth.config.config.Config')
celery = make_celery(app)

from app import views