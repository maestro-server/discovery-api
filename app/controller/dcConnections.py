
from app.controller.factory.dc import DcApp
from app.repository import Connections

class DcConnectionsApp(DcApp):
    def __init__(self):
        self.entity = Connections