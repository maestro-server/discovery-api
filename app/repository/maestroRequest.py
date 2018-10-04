
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
        self.__context = getattr(requests, self.__verb)(path, json=json, data=data, headers=self.__headers)
        return self

    def get_status(self):
        return self.__context.status_code

    def get_json(self):
        if self.__context.status_code is 200:
            return self.__context.json()

        logger.info("Request[CODE] - %s", self.get_status())
        raise ClientMaestroError(self.__context.text)
    
    def get_raw(self):
        if self.__context:
            logger.info("Request[CODE] - %s", self.get_status())
            return self.__context.text