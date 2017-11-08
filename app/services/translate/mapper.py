
from abc import ABC, abstractmethod

class Mapper(ABC):
    @abstractmethod
    def translate(self):
        pass