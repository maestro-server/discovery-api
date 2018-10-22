
from app.views import app
from app.libs.logger import logger
from .externalMaestro import ExternalMaestro
from app.repository.libs.notifyError import notify_error

class ExternalMaestroWS(ExternalMaestro):
    
    def __init__(self):
        base = app.config['MAESTRO_WEBSOCKET_URI']
        super().__init__(base)

    def auth_header(self):
        token = app.config['WS_SECRET']

        headers = {
            'Authorization': 'apikey %s' % token
        }

        self.set_headers(headers)
        return self