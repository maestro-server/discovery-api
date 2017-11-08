
from abc import ABC, abstractmethod
from pydash.objects import get

class Mapper(ABC):

    def __init__(self, command):
        self.command = command

    def switch(self, source, batch):
        return get(batch, source)

    def arrCatcher(self, source, batch):
        list = get(batch, source['field'], [])
        for item in list:
            if item[source['sKey']].lower() == source['s'].lower():
                return item[source['catcher']]


    def fctStorage(self, source, batch):
        pass

    def fctAuth(self, source, batch):
        pass

    @abstractmethod
    def translate(self):
        pass