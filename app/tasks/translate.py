
from app import celery
from app.services.translater import TranslateAPI
from app.services.iterators.iTranslate import IteratorTranslate
from .insert import task_insert
from .tracker import task_tracker
from .notification import task_notification


@celery.task(name="translate.api", serializer="pickle")
def task_translate(conn, conn_id, options, task, result, lasted=False):

    if not isinstance(result, list):
        task_notification.delay(msg="[Translate] Empty result", conn_id=conn_id, task=task, status='warning')
        return {'task': task}

    insert_id = []
    tracker_id = []

    connection = {**conn, 'id': conn_id}
    Translater = TranslateAPI(conn['service'], options, task, connection)
    GenerateTranslate = IteratorTranslate(result)

    for batch in GenerateTranslate.batch():
        translate = Translater.translate(batch)
        tlasted = lasted and GenerateTranslate.isLast()  # lasted of result and lasted of IteratorTranslate

        if translate:
            key = task_insert.delay(conn, conn_id, task, translate, options, tlasted)
            insert_id.append(str(key))

            tkey = task_tracker.delay(translate, conn['dc_id'], conn['region'], task, options)
            tracker_id.append(str(tkey))

    if len(insert_id) == 0:
        task_notification.delay(msg="[Translate] Empty result", conn_id=conn_id, task=task, status='warning')

    return {
        'insert-id': insert_id,
        'tracker-id': tracker_id,
        'conn_id': conn_id,
        'task': task
    }