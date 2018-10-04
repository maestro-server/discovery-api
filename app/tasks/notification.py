
import datetime
from app.views import app
from app import celery
from app.repository.externalMaestro import ExternalMaestro

@celery.task(name="notification.api")
def task_notification(msg, conn_id, task, status='success'):
    now = datetime.datetime.now()
    msg = "%s At %s" % (msg, now)

    base = app.config['MAESTRO_DATA_URI']
    body = {'status': status, 'task': task, 'msg': msg}

    ExternalMaestro(base)\
        .post_request(path="connection/%s" % conn_id, body=body)\
        .get_results()

    return {'conn_id': conn_id, 'task': task}