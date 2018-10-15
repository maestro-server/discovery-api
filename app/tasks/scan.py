
from app.views import app
from app import celery
from app.services.factory import FactoryAPI

from app.libs.jwt import Jwt
from app.libs.normalize import Normalize
from app.error import FactoryInvalid, ClientMaestroError

from .translate import task_translate
from .notification import task_notification
from .last import task_last


@celery.task(name="scan.api")
def task_scan(conn, conn_id, task, options, vars = []):
    try:
        access = Jwt.decode(conn['conn'])
    except Exception as error:
        task_notification.delay(msg=str(error), conn_id=conn_id, task=task, status='danger')
        return FactoryInvalid.responseInvalid(
            {'msg': str(error), 'name': error.__class__.__name__}
            , 403
        )


    oVars = Normalize.optionsVarsNormalize(options['vars']),
    vars = sum(oVars, vars)

    try:
        Crawler = FactoryAPI(access=access, conn=conn)
        result = Crawler.execute(options, vars)

        if not result['result']:
            raise ValueError('Empty result')

        factoryPag = Crawler.checkPag()
        key = task_translate.delay(conn, conn_id, options, task, result['result'])

        if factoryPag:
            task_scan.delay(conn, conn_id, task, options, [factoryPag])
        else:
            ctd = app.config['MAESTRO_COUNTDOWN_LAST']
            task_last.apply_async((conn, task, options), countdown=ctd)

        return {
            'translate-id': str(key),
            'conn_id': conn_id,
            'options': options,
            'next': factoryPag,
            'qtd': len(result['result'])
        }

    except Exception as error:
        status = 'warning'
        code = 500
        
        if error.__class__.__name__ == 'ClientMaestroError':
            status = 'danger'
            code = 403
        
        task_notification.delay(msg=str(error), conn_id=conn_id, task=task, status=status)
        return FactoryInvalid.responseInvalid(
            {'msg': str(error), 'name': error.__class__.__name__}
            , code
        )
