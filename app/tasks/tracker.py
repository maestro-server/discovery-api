
from app import celery
from pydash import get, slugify
from app.repository.externalMaestroData import ExternalMaestroData

@celery.task(name="tracker.api")
def task_tracker(result, dc_id, region, task):

    ids = list(map(lambda x: get(x, 'unique_id'), result))
    region = slugify(region)

    body = [{
        '_id': dc_id,
        '$addToSet': {
            "tracker.%s.%s" % (task, region): {'$each': ids}
        }
    }]

    ExternalMaestroData(entity_id=dc_id) \
        .put_request(path="datacenters", body={'body': body})

    return {'dc_id': dc_id, 'ids': ids}