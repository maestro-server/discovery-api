# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
import pymongo
from pymongo import MongoClient
from .celery import make_celery

app = Flask(__name__)
app.config.from_object('instance.config.Config')

client = MongoClient(app.config['DATABASE_URI'], serverSelectionTimeoutMS=1)
db = client[app.config['DATABASE_NAME']]

celery = make_celery(app)


try:
    client.server_info() # Forces a call.
    print("Mongo Online")
except pymongo.errors.ServerSelectionTimeoutError as err:
    print("==================================> MongoDB is down", err)