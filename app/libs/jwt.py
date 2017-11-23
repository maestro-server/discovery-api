
import jwt
from app import app

class Jwt(object):

    @staticmethod
    def decode(encoded):
        return jwt.decode(encoded, app.config['SECRETJWT'], algorithms=['HS256'])