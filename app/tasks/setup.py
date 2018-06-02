
import requests
from app import celery
from pydash import slugify
from app.libs.url import FactoryURL


@celery.task(name="setup.api")
def task_setup(dc_id, task, region):
    region = slugify(region)

    body = [{
        '_id': dc_id,
        '$unset': {
            "tracker.%s.%s" % (task, region): True
        }
    }]

    path = FactoryURL.make('datacenters')
    result = requests.put(path, json={'body': body})

    return {'code': result.status_code,  'dc_id': dc_id}