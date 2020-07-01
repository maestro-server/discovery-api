from app import celery
from pydash import get, slugify
from app.repository.externalMaestroData import ExternalMaestroData
from app.tasks.helpers.tracker import HelperQueryTracker


@celery.task(name="tracker.api")
def task_tracker(result, dc_id, region, task, accountant, options):
    ids = list(map(lambda x: get(x, options.get('key_comparer')), result))
    region = slugify(region)

    body = HelperQueryTracker() \
        .query('$addToSet') \
        .tracker(task, accountant, region) \
        .make_tracker(dc_id, {'$each': ids})

    result = ExternalMaestroData(entity_id=dc_id) \
        .put_request(path="datacenters", body={'body': body}) \
        .get_results()

    return {'dc_id': dc_id, 'result': result}
