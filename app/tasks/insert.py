
from app import celery


@celery.task(name="insert.api", bind=True)
def task_insert(self, conn_id, task, result):
    print("insert", result)
    return {'name': self.request.task, 'conn_id': conn_id, 'task': task, 'result': result}

