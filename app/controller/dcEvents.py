
from app.controller.factory.dc import DcApp
from app.repository import Events

class DcEventsApp(DcApp):
    def __init__(self):
        self.entity = Events