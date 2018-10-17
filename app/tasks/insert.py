
import json
from pydash.objects import get, has
from app import celery
from app.services.merger import MergeAPI
from app.repository.externalMaestroData import ExternalMaestroData
from .notification import task_notification


def get_data_list(result, key, owner_user, conn_id, entity):

    ids = [get(x, key) for x in result if has(x, key)]
    if not ids:
        raise PermissionError('[Insert Task] Key Comparer missing')

    query = json.dumps({key: ids, 'roles._id': owner_user})
    return ExternalMaestroData(entity_id=conn_id) \
        .post_request(path="%s" % (entity), body={'query': query}) \
        .get_results('items')



@celery.task(name="insert.api")
def task_insert(conn, conn_id, task, result, options):
    key = get(options, 'key_comparer')
    owner_user = get(conn, 'owner_user._id')

    if not owner_user:
        task_notification.delay(msg="Missing Owner User/Team in this connection.", conn_id=conn_id, task=task, status='danger')
        raise PermissionError('[Insert Task] Missing Owner')

    content = get_data_list(result, key, owner_user, conn_id, options['entity'])
    body = MergeAPI(content=content, key_comparer=key).merge(result)

    if len(body) > 0:
        ExternalMaestroData(entity_id=conn_id).put_request(path=options['entity'], body={'body': body})
        task_notification.delay(msg="Success.", conn_id=conn_id, task=task, status='success')

    task_notification.delay(msg="Success. No changes", conn_id=conn_id, task=task, status='success')

    return {'conn_id': conn_id, 'task': task, 'notification-id': str(key), 'body': len(body)}