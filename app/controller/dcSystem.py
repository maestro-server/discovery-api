
from app.controller.factory.dc import DcApp
from app.repository import Systems

class DcSystemnApp(DcApp):
    def __init__(self):
        self.entity = Systems