# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import os
from app.libs.jsonEncoder import DateTimeEncoder
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config(object):
    TESTING = os.environ.get("TESTING", False)
    SECRETJWT = os.environ.get("SECRETJWT", "baseFlaskSecretKey")
    DATABASE_URI = os.environ.get("MONGO_URL", False)
    DATABASE_NAME = os.environ.get("MONGO_DATABASE", False)
    RESTFUL_JSON = {'cls': DateTimeEncoder}
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", False)
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", False)
    CELERY_TASK_ROUTES = ([{'scan.*': {'queue': 'scan'}}])

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True