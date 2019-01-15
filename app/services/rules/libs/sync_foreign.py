
import json
from pydash.objects import pick
from app.libs.cache import CacheMemory
from app.repository.externalMaestroData import ExternalMaestroData

def sync_apps(tentity, source, key='name'):

    tentity = tentity.split(',')
    apps = []

    for tmp in tentity:
        tmp = tmp.strip()
        app = request_apps(tmp, source, key)
        if app:
            apps += app

    return apps


def request_apps(app, source, key):

    obj = CacheMemory.get(app)
    if not obj:
        query = json.dumps({key: app})
        results = ExternalMaestroData() \
            .post_request(path=source, body={'query': query}) \
            .get_results('items')

        if results:
            obj = shrink_arr(results)
            CacheMemory.set(app, obj)

    return obj

def shrink_arr(results):
    sapps = []

    for result in results:
        app = pick(result, ['_id', 'name', 'family'])
        sapps.append(app)

    return sapps