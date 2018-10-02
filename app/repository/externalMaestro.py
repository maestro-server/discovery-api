import json
from app.libs.logger import logger
from .maestroRequest import MaestroRequest

class ExternalMaestro(object):

    def __init__(self, base, entity_id=None, owner_id=None):
        self._base = base
        self._owner_id = owner_id
        self._entity_id = entity_id
        self._headers = {}

    def get_uri(self):
        self._base

    def make_filter(self, filter, active=True):
        base = {'active': active}

        if self._owner_id:
            base['roles._id'] = self._owner_id

        if any(filter) and isinstance(filter, dict):
            return {**base, **filter}

        return base


    def get_request(self, path, query={}, active=True):
        merged = self.make_filter(query, active)

        jquery = json.dumps(merged)
        return self.request(path, {'query': jquery}, 'get').get_results()

    def get_aggregation(self, path, entity, pipeline):
        jpipeline = json.dumps(pipeline)
        return self.request(path, {'entity': entity, 'pipeline': jpipeline}).get_results()

    def put_request(self, path, body={}):
        return self.request(path, body, 'put').get_raw()

    def post_request(self, path, body={}):
        return self.request(path, body, 'post').get_raw()
    
    def request(self, path, query, verb='post'):
        path = "%s/%s" % (self._base, path)
        MaestroRqt = MaestroRequest().set_headers(self._headers)

        try:
            MaestroRqt.exec_request(path, query, verb)
            logger.debug("MaestroRequest External path - %s", path)
        except Exception as error:
            self.error_handling(task='ExternalMaestro', entity_id=self._entity_id, msg=str(error))

        return MaestroRqt

    def set_headers(self, headers):
        self._headers = headers
        return self

    def error_handling(self, task, entity_id, msg):
        logger.error("Discovery:  [%s][%s] - %s", task, entity_id, msg)