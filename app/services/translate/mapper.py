
from abc import ABC, abstractmethod
from pydash.objects import get

class Mapper(ABC):

    def __init__(self, command, conn):
        self.command = command
        self.conn = conn

    @abstractmethod
    def translate(self):
        pass