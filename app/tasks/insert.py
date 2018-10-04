
import json
from pydash.objects import get
from app import celery
from app.services.merger import MergeAPI
from app.repository.externalMaestroData import ExternalMaestroData

from .notification import task_notification


@celery.task(name="insert.api")
def task_insert(conn, conn_id, task, result, options):
    query = None
    key = get(options, 'key_comparer')
    owner_user = get(conn, 'owner_user._id')

    if not owner_user:
        task_notification.delay(msg="Missing Owner User/Team in this connection.", conn_id=conn_id, task=task, status='danger')
        raise PermissionError('Missing Owner')

    ids = list(map(lambda x: get(x, key), result))
    if ids:
        query = json.dumps({key: ids, 'roles._id': owner_user})

    content = ExternalMaestroData(entity_id=conn_id)\
        .post_request(path="%s" % (options['entity']), body={'query': query})\
        .get_results('items')

    body = MergeAPI(content=content, key_comparer=key).merge(result)

    if len(body) > 0:
        ExternalMaestroData(entity_id=conn_id).put_request(path=options['entity'], body={'body': body})
        key = task_notification.delay(msg="Success.", conn_id=conn_id, task=task, status='success')

    key = task_notification.delay(msg="Success. No changes", conn_id=conn_id, task=task, status='success')

    return {'conn_id': conn_id, 'task': task, 'notification-id': str(key), 'body': len(body)}