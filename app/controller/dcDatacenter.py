
from app.controller.factory.dc import DcApp
from app.repository import Datacenters

class DcDatacentersApp(DcApp):
    def __init__(self):
        self.entity = Datacenters