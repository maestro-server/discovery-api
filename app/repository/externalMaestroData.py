
from app.views import app
from .externalMaestro import ExternalMaestro
from app.libs.notifyError import notify_error

class ExternalMaestroData(ExternalMaestro):
    
    def __init__(self, entity_id=None, owner_id=None):
        base = app.config['MAESTRO_DATA_URI']
        super().__init__(base, entity_id, owner_id)

    def error_handling(self, task, owner_id, graph_id, msg):
        return notify_error(task, owner_id, graph_id, msg)