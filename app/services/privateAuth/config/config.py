# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""


from app.services.privateAuth.libs.addPrivateAuthToken import createToken

class Config(object):
    PRIVATE_HEADER_TOKEN = createToken()