
import json
from app import celery
from app.repository.externalMaestroData import ExternalMaestroData

@celery.task(name="last.api")
def task_last(conn, task):

    query = json.dumps({'_id': conn['dc_id']})
    result = ExternalMaestroData() \
        .post_request(path="datacenters", body={'query': query}) \
        .get_results('items')

    if result:
        lists = result.pop().get('tracker').get(task)
    print(lists, conn, task)

    return {'dc_id': conn['dc_id'], 'task': task}