
import requests, datetime
from app import celery
from app.libs.url import FactoryURL

@celery.task(name="notification.api", bind=True)
def task_notification(self, msg, conn_id, task, status = 'success'):
    now = datetime.datetime.now()
    msg = "%s At %s" % (msg, now)

    path = FactoryURL.make(path="connection/%s" % conn_id)
    requests.post(path, json={'status': status, 'task': task, 'msg': msg})

    return {'name': self.request.task, 'conn_id': conn_id, 'task': task}