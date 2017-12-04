
from app.controller.factory.dc import DcApp
from app.repository import Networks

class DcNetworkApp(DcApp):
    def __init__(self):
        self.entity = Networks