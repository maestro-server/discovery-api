
import os
from app import celery
from app.services.translater import TranslateAPI
from .insert import task_insert



@celery.task(name="translate.api", bind=True)
def task_translate(self, conn_id, commands, provider, result):
    limit = os.environ.get("MAESTRO_TRANSLATE_QTD", 100)

    Translater = TranslateAPI(provider, commands['access'], limit)

    for batch in Translater.translate(result['result']):
        print(len(batch))

    print(commands)

    key = task_insert.delay(conn_id, result)
    return {'name': self.request.task, 'insert-id': str(key), 'conn_id': conn_id, 'provider': provider, 'commands': commands}