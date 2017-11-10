
from app import celery
from app.services.factory import FactoryAPI

from app.libs.jwt import Jwt
from app.error import FactoryInvalid, ClientMaestroError, MissingError

from .translate import task_translate


@celery.task(name="scan.api", bind=True)
def task_scan(self, conn, id, task, commands, filter=[], pagination=[]):
    access = Jwt.decode(conn['conn'])

    try:
        result = FactoryAPI(access=access, dc=conn['provider'], region=conn['region']).execute(commands)
        key = task_translate.delay(conn, id, commands, task, result)

        return {
            'name': self.request.task,
            'translate-id': str(key),
            'conn_id': id,
            'commands': commands,
            **conn
        }

    except (ClientMaestroError, MissingError) as error:
        return FactoryInvalid.responseInvalid(
            {'name': self.request.task, 'msg': str(error), 'name': error.__class__.__name__}
            , 403
        )

    except Exception as error:
        return FactoryInvalid.responseInvalid(
            {'name': self.request.task, 'msg': str(error), 'name': error.__class__.__name__}
            , 500
        )
