
from app.views import app
from .externalMaestro import ExternalMaestro

from app.services.privateAuth.decorators.external_private_token import add_external_header_auth

@add_external_header_auth
class ExternalMaestroAudit(ExternalMaestro):
    
    def __init__(self):
        base = app.config['MAESTRO_AUDIT_URI']
        super().__init__(base)

        self.private_auth_header()