# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app.services.privateAuth.libs.addPrivateAuthToken import create_token


class Config(object):
    PRIVATE_HEADER_TOKEN = create_token()
