
import os
from app import celery
from app.services.translater import TranslateAPI
from app.services.batcher import BatchAPI
from .insert import task_insert


@celery.task(name="translate.api", bind=True)
def task_translate(self, conn_id, commands, task, provider, result):
    limit = os.environ.get("MAESTRO_TRANSLATE_QTD", 50)
    insert_id = []

    Translater = TranslateAPI(provider, commands['access'], task)

    for batch in BatchAPI(limit).batch(result['result']):
        translate = Translater.translate(batch)
        return translate
        key = task_insert.delay(conn_id, task, translate)
        insert_id.append(str(key))

    return {'name': self.request.task, 'insert-id': insert_id, 'conn_id': conn_id, 'task': task, 'provider': provider, 'commands': commands}