
import os
from app import celery
from app.services.translater import TranslateAPI
from app.services.iterators.iTranslate import IteratorTranslate
from .insert import task_insert
from .tracker import task_tracker


@celery.task(name="translate.api", bind=True)
def task_translate(self, conn, conn_id, options, task, result):
    limit = os.environ.get("MAESTRO_TRANSLATE_QTD", 50)
    insert_id = []
    tracker_id = []

    connection = {**conn, 'id': conn_id}
    Translater = TranslateAPI(conn['provider'], options, task, connection)

    for batch in IteratorTranslate(limit).batch(result):
        translate = Translater.translate(batch)
        key = task_insert.delay(conn, conn_id, task, translate, options)
        tkey = task_tracker.delay(translate, conn['dc_id'])
        insert_id.append(str(key))
        tracker_id.append(str(tkey))

    return {'name': self.request.task, 'insert-id': insert_id, 'tracker-id': tracker_id, 'conn_id': conn_id, 'task': task}