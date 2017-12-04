
from app.controller.factory.dc import DcApp
from app.repository import Snapshots

class DcSnapshotsApp(DcApp):
    def __init__(self):
        self.entity = Snapshots