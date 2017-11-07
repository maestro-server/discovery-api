
from abc import ABC, abstractmethod

class Connector(ABC):
    @abstractmethod
    def credencials(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def execute(self):
        pass