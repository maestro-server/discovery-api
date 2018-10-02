
from app import celery
from pydash import slugify
from app.repository.externalMaestroData import ExternalMaestroData


@celery.task(name="setup.api")
def task_setup(dc_id, task, region):
    region = slugify(region)

    body = [{
        '_id': dc_id,
        '$unset': {
            "tracker.%s.%s" % (task, region): True
        }
    }]

    ExternalMaestroData(entity_id=dc_id)\
        .put_request(path="datacenters", body={'body': body})

    return {'dc_id': dc_id}