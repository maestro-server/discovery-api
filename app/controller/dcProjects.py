
from app.controller.factory.dc import DcApp
from app.repository import Projects

class DcProjectsApp(DcApp):
    def __init__(self):
        self.entity = Projects