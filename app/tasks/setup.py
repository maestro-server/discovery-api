from app import celery
from pydash import slugify
from app.repository.externalMaestroData import ExternalMaestroData
from app.tasks.helpers.tracker import HelperQueryTracker


@celery.task(name="setup.api")
def task_setup(dc_id, task, accountant, region):
    region = slugify(region)

    body = HelperQueryTracker() \
        .query('$unset') \
        .tracker(task, accountant, region) \
        .make_tracker(dc_id, True)

    ExternalMaestroData(entity_id=dc_id) \
        .put_request(path="datacenters", body={'body': body})

    return {'dc_id': dc_id}
