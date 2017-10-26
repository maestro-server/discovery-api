
import jwt
from jwt.exceptions import DecodeError
from app import app

class Jwt(object):

    @staticmethod
    def decode(encoded):

        try:
            response = jwt.decode(encoded, app.config['SECRETJWT'], algorithms=['HS256'])
        except DecodeError:
            response = {'error': 'Invalid Token', 'status': 403}
        except:
            response = {'error': 'Jwt decode error', 'status': 500}

        return response