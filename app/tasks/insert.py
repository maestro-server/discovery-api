
import os, json, requests
from urllib.parse import urlencode, quote_plus
from pydash.objects import get
from app import celery
from app.services.merger import MergeAPI

requests.get('https://api.github.com/user', auth=('user', 'pass'))


@celery.task(name="insert.api", bind=True)
def task_insert(self, conn_id, task, result):
    query = None
    url = os.environ.get("DISCOVERY_URL", "localhost")

    ids = map(lambda x: get(x, 'datacenters.instance_id'), result)
    if ids:
        query = json.dumps({'datacenters.instance_id': list(ids)})

    url_values = urlencode({'query': query}, quote_via=quote_plus)
    resource = requests.get("http://%s/servers?%s" % (url, url_values))
    content = resource.json()
    content = get(content, 'items')

    body = MergeAPI(content).merge(result)

    resource = requests.put("http://%s/servers" % (url), json={'body': body})

    print(resource.text)



    return {'name': self.request.task, 'conn_id': conn_id, 'task': task, 'result': resource.text}

