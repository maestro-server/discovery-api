import jwt
from app import app
from flask import request
from app.services.privateAuth.error.privateUnauthorized import PrivateUnauthorizedError


class PrivateAuth(object):
    @staticmethod
    def autheticate():
        auth_token = None
        auth_header = request.headers.get('Authorization')

        if auth_header:
            auth_token = auth_header.split(" ")[1]

        if auth_token:
            resp = PrivateAuth.decode(auth_token)

            if resp.get('noauth') == app.config['NOAUTH']:
                return resp

        raise PrivateUnauthorizedError('Unauthorized')

    @staticmethod
    def create_token(info):
        body = {
            **info,
            'noauth': app.config['NOAUTH']
        }

        return PrivateAuth.encode(body)

    @staticmethod
    def encode(body):
        return jwt.encode(body, app.config['SECRETJWT_PRIVATE'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def decode(encoded):
        return jwt.decode(encoded, app.config['SECRETJWT_PRIVATE'], algorithms=['HS256'])
