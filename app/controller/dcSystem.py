
from app.controller.factory.dc import DcApp
from app.repository import Systems

class DcSystemApp(DcApp):
    def __init__(self):
        self.entity = Systems