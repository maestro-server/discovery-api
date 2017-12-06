
from app.controller.factory.dc import DcApp
from app.repository import Flavors

class DcFlavorsApp(DcApp):
    def __init__(self):
        self.entity = Flavors