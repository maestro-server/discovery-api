import requests
from app.libs.logger import logger
from app.error.clientMaestroError import ClientMaestroError


class MaestroRequest(object):
    def __init__(self, verb='get', headers={}):
        self.__context = None
        self.__headers = headers
        self.__path = None
        self.__verb = verb

    def exec_request(self, path, json=None, data=None):
        self.__path = path
        self.__context = getattr(requests, self.__verb)(path, json=json, data=data, headers=self.__headers)
        self.raiseError()

        return self

    def get_status(self):
        return self.__context.status_code

    def raiseError(self):
        msg = ''

        if self.get_status() < 400:
            return False

        if self.get_status() >= 400:
            msg = self.__context.text

        if self.get_status() in [0]:
            msg = "Service not found"

        logger.info("Error %s", msg)
        raise ClientMaestroError(msg)

    def get_json(self):

        if self.__context:
            logger.info("Request[CODE %s] - %s", self.get_status(), self.__path)
            return self.__context.json()

