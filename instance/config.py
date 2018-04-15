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
    SECRETJWT = os.environ.get("MAESTRO_SECRETJWT", "defaultSecretKey")
    RESTFUL_JSON = {'cls': DateTimeEncoder}
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'amqp://localhost')
    CELERY_DEFAULT_QUEUE = 'discovery'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
