# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('instance.config.Config')

client = MongoClient(app.config['DATABASE_URI'])
db = client['maestro']

from app import views