import json
from app.libs.logger import logger
from .maestroRequest import MaestroRequest


class ExternalMaestro(object):
    def __init__(self, base, tftm="json", requester=MaestroRequest):
        self._base = base
        self._headers = {}
        self._results = None
        self._format = tftm
        self._requester = requester

    def set_headers(self, headers):
        self._headers = headers
        return self

    def set_fomart(self, format):
        self._format = format
        return self

    def get_results(self, lens=None, default=[]):
        results = self._results.get_json()
        if results and lens:
            results = results.get(lens, default)

        return results

    def list_request(self, path, query={}):
        self._results = self.request(path, {'query': query}, 'get')
        return self

    def list_aggregation(self, path, entity, pipeline):
        jpipeline = json.dumps(pipeline)
        self._results = self.request(path, {'entity': entity, 'pipeline': jpipeline}, 'post')
        return self

    def put_request(self, path, body={}):
        self._results = self.request(path, body, 'put')
        return self

    def post_request(self, path, body={}):
        self._results = self.request(path, body, 'post')
        return self

    def request(self, path, query, verb):

        MaestroRqt = self._requester(verb, self._headers)
        params = {
            'path': "%s/%s" % (self._base, path),
            self._format: query
        }

        try:
            MaestroRqt.exec_request(**params)
            logger.debug("MaestroRequest External path - %s", path)
        except Exception as error:
            self.error_handling(task='ExternalMaestro', msg=str(error))

        return MaestroRqt

    def error_handling(self, task, msg):
        logger.error("MaestroExternal:  [%s] - %s", task, msg)