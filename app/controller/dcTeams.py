
from app.controller.factory.dc import DcApp
from app.repository import Teams

class DcTeamsApp(DcApp):
    def __init__(self):
        self.entity = Teams