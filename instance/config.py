# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import os

class InstanceConfig(object):
    TESTING = os.environ.get("TESTING", False)
    SECRET_KEY = os.environ.get("SECRET_KEY", "baseFlaskSecretKey")
    DATABASE_URI = os.environ.get("MONGO_URL", False)