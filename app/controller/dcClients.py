
from app.controller.factory.dc import DcApp
from app.repository import Clients

class DcClientsApp(DcApp):
    def __init__(self):
        self.entity = Clients