
from pydash.objects import get
from app import celery
from app.repository.externalMaestroWS import ExternalMaestroWS

@celery.task(name="ws.api")
def task_ws(conn, conn_id, task, status='success'):
    owner_id = get(conn, 'owner_user._id')
    dc_name = get(conn, 'dc')
    provider = get(conn, 'provider')

    msg = "Finish Sync - [%s] %s" % (provider, task)
    channel = "maestro-%s" % owner_id

    body = {
        "method": "publish",
        "params": {
            "channel": channel,
            "data": {
                "notify": {
                    "title": dc_name,
                    "msg": msg,
                    "type": status
                },
                "event": {
                    "caller": ["connections-update", "connections-{}".format(conn_id)]
                }
            }
        }
    }

    try:
        result = ExternalMaestroWS() \
            .auth_header() \
            .post_request(path="api", body=body) \
            .get_results()

        return {'result': result, 'task': 'ws-notification'}

    except Exception as error:
        return {'message': str(error)}