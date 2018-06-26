
import requests
from app import celery
from pydash import get, slugify
from app.libs.url import FactoryURL

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

    path = FactoryURL.make('datacenters')

    try:
        result = requests.put(path, json={'body': body})
        return {'code': result.status_code,  'dc_id': dc_id, 'ids': ids}
    except requests.exceptions.RequestException as error:
        return {'error': str(error)}

    
