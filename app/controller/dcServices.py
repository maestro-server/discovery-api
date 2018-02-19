
from app.controller.factory.dc import DcApp
from app.repository import Services

class DcServicesApp(DcApp):
    def __init__(self):
        self.entity = Services