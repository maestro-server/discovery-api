
from app.controller.factory.dc import DcApp
from app.repository import Reports

class DcReportsApp(DcApp):
    def __init__(self):
        self.entity = Reports