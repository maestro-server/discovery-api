
from app.controller.factory.dc import DcApp
from app.repository import Servers

class DcServersApp(DcApp):
    def __init__(self):
        self.entity = Servers