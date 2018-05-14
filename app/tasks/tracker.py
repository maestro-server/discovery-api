
from app import celery
from pydash import get


@celery.task(name="tracker.api", bind=True)
def task_tracker(self, result, dc_id):

    ids = list(map(lambda x: get(x, 'unique_id'), result))


    print(ids)
    print(dc_id)

    return {}