# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config(object):
    TESTING = os.environ.get("TESTING", False)
    SECRETJWT = os.environ.get("SECRETJWT", "baseFlaskSecretKey")
    DATABASE_URI = os.environ.get("MONGO_URL", False)
    DATABASE_NAME = os.environ.get("MONGO_DATABASE", False)


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True