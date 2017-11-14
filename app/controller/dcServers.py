
from app.controller.factory.dc import DcApp
from app.models import Servers

class DcServersApp(DcApp):
    def __init__(self):
        self.entity = Servers