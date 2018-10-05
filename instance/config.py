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

    MAESTRO_DATA_URI = os.environ.get("MAESTRO_DATA_URI", "http://localhost:5010")
    MAESTRO_COUNTDOWN_LAST = int(os.environ.get("MAESTRO_COUNTDOWN_LAST", 60))
    MAESTRO_TRANSLATE_QTD = int(os.environ.get("MAESTRO_TRANSLATE_QTD", 50))

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'amqp://localhost')
    CELERY_DEFAULT_QUEUE = 'discovery'