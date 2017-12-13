
import json, requests
from pydash.objects import get
from app import celery
from app.services.merger import MergeAPI
from app.libs.url import FactoryURL

from .notification import task_notification


@celery.task(name="insert.api", bind=True)
def task_insert(self, conn, conn_id, task, result, options):
    query = None
    key = get(options, 'key_comparer')
    owner_user = get(conn, 'owner_user._id')

    if not owner_user:
        task_notification.delay(msg="Missing Owner User/Team in this connection.", conn_id=conn_id, task=task, status='danger')
        raise PermissionError('Missing Owner')

    content = []

    ids = list(map(lambda x: get(x, key), result))
    if ids:
        query = json.dumps({key: ids, 'roles._id': owner_user})

    path = FactoryURL.make(path="%s" % (options['entity']))
    resource = requests.post(path, json={'query': query})

    content = resource.json()

    content = get(content, 'items')
    body = MergeAPI(content=content, key_comparer=key).merge(result)

    path = FactoryURL.make(path=options['entity'])
    resource = requests.put(path, json={'body': body})

    key = task_notification.delay(msg="Success.", conn_id=conn_id, task=task, status='success')

    return {'name': self.request.task, 'conn_id': conn_id, 'task': task, 'notification-id': str(key), 'result': resource.text}