
from app.views import app
from app import celery
from app.services.translater import TranslateAPI
from app.services.iterators.iTranslate import IteratorTranslate
from .insert import task_insert
from .tracker import task_tracker
from .notification import task_notification


@celery.task(name="translate.api")
def task_translate(conn, conn_id, options, task, result):
    limit = app.config['MAESTRO_TRANSLATE_QTD']
    insert_id = []
    tracker_id = []

    connection = {**conn, 'id': conn_id}
    Translater = TranslateAPI(conn['provider'], options, task, connection)

    if not isinstance(result, list):
        task_notification.delay(msg="Empty", conn_id=conn_id, task=task, status='warning')
        return {'task': task}

    for batch in IteratorTranslate(limit).batch(result):
        translate = Translater.translate(batch)
        key = task_insert.delay(conn, conn_id, task, translate, options)
        tkey = task_tracker.delay(translate, conn['dc_id'], conn['region'], task, options)
        insert_id.append(str(key))
        tracker_id.append(str(tkey))

    return {'insert-id': insert_id, 'tracker-id': tracker_id, 'conn_id': conn_id, 'task': task}

