
from app import app

def create_jwt():
    token = app.config['PRIVATE_HEADER_TOKEN']

    return {
        'Authorization': 'JWT %s' % token
    }

def private_auth_header(self):
    headers = create_jwt()
    self.set_headers(headers)
    return self

def add_external_header_auth(cls):

    def wrapper(*args, **kargs):
        setattr(cls, 'private_auth_header', private_auth_header)
        return cls(*args, **kargs)

    return wrapper