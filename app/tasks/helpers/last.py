
import json
from pydash import slugify
from app.repository.externalMaestroData import ExternalMaestroData


def get_tracker(dc_id, task, region):
    dps = json.dumps({'_id': dc_id})

    return ExternalMaestroData() \
        .post_request(path="datacenters", body={'query': dps}) \
        .get_results('items') \
        .pop() \
        .get('tracker', {}) \
        .get(task, {}) \
        .get(slugify(region), [])

def make_query(dc_id, region, lst, options):
    key_comparer = options.get('key_comparer')
    family = options.get('family')
    provider = options.get('provider')

    query = {
        'datacenters._id': dc_id,
        'active': True
    }

    if lst:
        query[key_comparer] = {'$nin': lst}

    if region != 'all':
        query['datacenters.region'] = region

    if family:
        query['family'] = family

    if provider:
        query['provider'] = provider

    return json.dumps(query)

def make_body():
    return json.dumps({'active': False})

def entity_count(dc_id, region, lst, options):

    body = {
        'entity': options.get('entity'),
        'query': make_query(dc_id, region, lst, options),
        'body': make_body()
    }

    return ExternalMaestroData() \
        .post_request(path="sync", body=body) \
        .get_results()