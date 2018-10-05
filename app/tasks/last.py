
import json
from app import celery
from pydash import slugify
from app.libs.logger import logger
from app.repository.externalMaestroData import ExternalMaestroData


def get_tracker(dc_id, task, region):
    dps = json.dumps({'_id': dc_id})

    return ExternalMaestroData() \
        .post_request(path="datacenters", body={'query': dps}) \
        .get_results('items') \
        .pop() \
        .get('tracker', {}) \
        .get(task, {}) \
        .get(slugify(region))

def entity_count(dc_id, region):
    dps = json.dumps({'datacenters._id': dc_id, 'datacenters.region': region, 'active': True})

    return ExternalMaestroData() \
        .post_request(path="servers", body={'query': dps}) \
        .get_results('found')

def sync_inconsistenc(lst):
    print(lst)

    return ExternalMaestroData() \
        .put_request(path="servers", body={'query': dps}) \
        .get_results()

@celery.task(name="last.api")
def task_last(conn, task):

    dc_id = conn.get('dc_id')
    region = conn.get('region')

    result = get_tracker(dc_id, task, region)
    if result:
        counts = entity_count(dc_id, region)

        dc_counts = len(result)
        if dc_counts != counts:
            result = sync_inconsistenc(result)
            logger.info("SYNC - [%s] [%s]", dc_counts, counts)
            logger.info(result)

    return {'dc_id': dc_id, 'task': task}