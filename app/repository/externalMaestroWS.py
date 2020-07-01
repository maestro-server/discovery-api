from app.views import app
from .externalMaestro import ExternalMaestro


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
