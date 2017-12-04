
from app import celery
from app.services.factory import FactoryAPI

from app.libs.jwt import Jwt
from app.libs.optionsVarsNormalize import optionsVarsNormalize
from app.error import FactoryInvalid, ClientMaestroError, MissingError

from .translate import task_translate
from .notification import task_notification


@celery.task(name="scan.api", bind=True)
def task_scan(self, conn, conn_id, task, options, vars = []):
    try:
        access = Jwt.decode(conn['conn'])
    except Exception as error:
        task_notification.delay(msg=str(error), conn_id=conn_id, task=task, status='danger')


    oVars = optionsVarsNormalize(options['vars']),
    vars = sum(oVars, vars)

    try:
        Crawler = FactoryAPI(access=access, conn=conn)
        result = Crawler.execute(options, vars)

        if not result['result']:
            raise ValueError('Empty result')

        factoryPag = Crawler.checkPag()
        if factoryPag:
            task_scan.delay(conn, conn_id, task, options, [factoryPag])

        key = task_translate.delay(conn, conn_id, options, task, result['result'])

        return {
            'name': self.request.task,
            'translate-id': str(key),
            'conn_id': conn_id,
            'options': options,
            'qtd': len(result['result'])
        }

    except (ClientMaestroError, MissingError) as error:

        task_notification.delay(msg=str(error), conn_id=conn_id, task=task, status='danger')

        return FactoryInvalid.responseInvalid(
            {'name': self.request.task, 'msg': str(error), 'name': error.__class__.__name__}
            , 403
        )

    except Exception as error:
        task_notification.delay(msg=str(error), conn_id=conn_id, task=task, status='warning')

        return FactoryInvalid.responseInvalid(
            {'name': self.request.task, 'msg': str(error), 'name': error.__class__.__name__}
            , 500
        )

