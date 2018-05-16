
import requests
from app import celery
from pydash import get
from app.libs.url import FactoryURL

@celery.task(name="tracker.api", bind=True)
def task_tracker(self, result, dc_id):

    ids = map(lambda x: get(x, 'unique_id'), result)

    body = [{
        '_id': dc_id,
        '$addToSet': {'tracker': {'$each': list(ids)}}
    }]

    path = FactoryURL.make('datacenters')
    result = requests.put(path, json={'body': body})

    return {'code': result.status_code,  'dc_id': dc_id, 'ids': ids}