
from app.controller.factory.dc import DcApp
from app.repository import Images

class DcImagesApp(DcApp):
    def __init__(self):
        self.entity = Images