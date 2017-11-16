
import os
from app import celery
from app.services.translater import TranslateAPI
from app.services.iterators.iTranslate import IteratorTranslate
from .insert import task_insert


@celery.task(name="translate.api", bind=True)
def task_translate(self, conn, conn_id, options, task, result):
    limit = os.environ.get("MAESTRO_TRANSLATE_QTD", 50)
    insert_id = []

    connection = {**conn, 'id': conn_id}
    Translater = TranslateAPI(conn['provider'], options, task, connection)

    for batch in IteratorTranslate(limit).batch(result):
        translate = Translater.translate(batch)
        key = task_insert.delay(conn, conn_id, task, translate, options)
        insert_id.append(str(key))

    return {'name': self.request.task, 'insert-id': insert_id, 'conn_id': conn_id, 'task': task}