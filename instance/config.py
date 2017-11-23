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
    DATABASE_URI = "mongodb://" + os.environ.get("MAESTRO_MONGO_URI", "localhost")
    DATABASE_NAME = os.environ.get("MAESTRO_MONGO_DATABASE", "maestro")
    RESTFUL_JSON = {'cls': DateTimeEncoder}
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'amqp://localhost')
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", False)
    CELERY_TASK_ROUTES = ([{'scan.*': {'queue': 'scan'},'translate.*': {'queue': 'translate'},'notification.*': {'queue': 'notification'},'insert.*': {'queue': 'insert'}}])


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
