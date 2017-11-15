
import json, requests
from urllib.parse import urlencode, quote_plus
from pydash.objects import get
from app import celery
from app.services.merger import MergeAPI
from app.libs.url import FactoryURL

requests.get('https://api.github.com/user', auth=('user', 'pass'))


@celery.task(name="insert.api", bind=True)
def task_insert(self, conn_id, task, result, options):
    query = None
    key = get(options, 'key_comparer')
    content = []

    ids = list(map(lambda x: get(x, key), result))
    if ids:
        query = json.dumps({key: ids})

    url_values = urlencode({'query': query}, quote_via=quote_plus)
    path = FactoryURL.make(path="%s?%s" % (options['entity'], url_values))
    resource = requests.get(path)
    content = resource.json()
    content = get(content, 'items')

    body = MergeAPI(content=content, key_comparer=key).merge(result)

    path = FactoryURL.make(path=options['entity'])
    resource = requests.put(path, json={'body': body})

    return {'name': self.request.task, 'conn_id': conn_id, 'task': task, 'result': resource.text}