# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('instance.config.InstanceConfig')

from app import views