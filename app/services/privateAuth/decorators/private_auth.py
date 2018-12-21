import jwt
from functools import wraps
from app.services.privateAuth.auth import PrivateAuth
from app.error.factoryInvalid import FactoryInvalid
from app.services.privateAuth.error.privateUnauthorized import PrivateUnauthorizedError

def private_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            PrivateAuth.autheticate()
            return f(*args, **kwargs)

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, PrivateUnauthorizedError) as error:
            return FactoryInvalid.responseInvalid({'msg': str(error)}, 401)

    return decorated_function