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
    RESTFUL_JSON = {'cls': DateTimeEncoder}

    SECRETJWT = os.environ.get("MAESTRO_SECRETJWT", "defaultSecretKey")
    WS_SECRET = os.environ.get("MAESTRO_WEBSOCKET_SECRET", "wsSecretKey")

    SECRETJWT_PRIVATE = os.environ.get("MAESTRO_SECRETJWT_PRIVATE", "defaultSecretKeyPrivate")
    NOAUTH = os.environ.get("MAESTRO_NOAUTH", "defaultSecretNoAuthToken")

    MAESTRO_DATA_URI = os.environ.get("MAESTRO_DATA_URI", "http://localhost:5010")
    MAESTRO_AUDIT_URI = os.environ.get("MAESTRO_AUDIT_URI", "http://localhost:10900")
    MAESTRO_WEBSOCKET_URI = os.environ.get("MAESTRO_WEBSOCKET_URI", "http://localhost:8000")

    MAESTRO_COUNTDOWN_LAST = int(os.environ.get("MAESTRO_COUNTDOWN_LAST", 10))
    MAESTRO_COUNTDOWN_WS = int(os.environ.get("MAESTRO_COUNTDOWN_WS", 2))
    MAESTRO_TRANSLATE_QTD = int(os.environ.get("MAESTRO_TRANSLATE_QTD", 50))

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'amqp://localhost')
    CELERY_DEFAULT_QUEUE = 'discovery'
    CELERY_TASK_SERIALIZER = "json"
    CELERY_ACCEPT_CONTENT = ['pickle', 'json']