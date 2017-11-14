
from app import celery
from app.services.factory import FactoryAPI

from app.libs.jwt import Jwt
from app.error import FactoryInvalid, ClientMaestroError, MissingError

from .translate import task_translate


@celery.task(name="scan.api", bind=True)
def task_scan(self, conn, conn_id, task, options):
    access = Jwt.decode(conn['conn'])

    try:
        result = FactoryAPI(access=access, dc=conn['provider'], region=conn['region']).execute(options)

        if not result['result']:
            raise ValueError('Empty result')

        key = task_translate.delay(conn, conn_id, options, task, result['result'])

        return {
            'name': self.request.task,
            'translate-id': str(key),
            'conn_id': conn_id,
            'options': options,
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

