
from app import celery
from .helpers.last import get_tracker, entity_count


@celery.task(name="last.api")
def task_last(conn, task, options):
    dc_id = conn.get('dc_id')
    region = conn.get('region')
    owner = conn.get('owner_user').get('_id')

    result = get_tracker(dc_id, task, region)
    counts = entity_count(dc_id, owner, region, result, options)

    return {'sync': counts, 'dc_id': dc_id, 'task': task}
