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


def entity_count(dc_id, region, lst, options):
    entity = options.get('entity')
    key_comparer = options.get('key_comparer')

    query = {
        'datacenters._id': dc_id,
        'datacenters.region': region,
        'active': True
    }
    query[key_comparer] = {'$nin': lst}
    body = {'active': False}

    return ExternalMaestroData() \
        .post_request(path="sync", body={'entity': entity, 'query': json.dumps(query), 'body': json.dumps(body)}) \
        .get_results()


@celery.task(name="last.api")
def task_last(conn, task, options):
    dc_id = conn.get('dc_id')
    region = conn.get('region')

    result = get_tracker(dc_id, task, region)
    if result:
        counts = entity_count(dc_id, region, result, options)

        logger.info("SYNC - [%s]", counts)
        logger.info(counts)

    return {'dc_id': dc_id, 'task': task}
