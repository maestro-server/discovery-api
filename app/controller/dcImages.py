
from app.controller.factory.dc import DcApp
from app.repository import Volumes

class DcVolumesApp(DcApp):
    def __init__(self):
        self.entity = Volumes