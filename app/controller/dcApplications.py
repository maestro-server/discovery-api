
from app.controller.factory.dc import DcApp
from app.models import Applications

class DcApplicationApp(DcApp):
    def __init__(self):
        self.entity = Applications