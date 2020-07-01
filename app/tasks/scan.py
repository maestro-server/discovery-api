from types import GeneratorType
from app import app
from app import celery
from app.services.factory import FactoryAPI

from app.libs.decodeConn import decodeConn
from app.libs.normalize import Normalize
from app.error import FactoryInvalid

from .translate import task_translate
from .notification import task_notification
from .last import task_last
from .ws import task_ws


def iterTranslate(conn, conn_id, options, task, result, tlasted):
    if isinstance(result, list):
        return task_translate.delay(conn, conn_id, options, task, result, tlasted)

    if isinstance(result, GeneratorType):
        for generator in result:
            iterTranslate(conn, conn_id, options, task, generator, tlasted)
        return

    if hasattr(result, '__iter__'):  # get chunk of iterator, transform to list and send for translate task
        iterTranslate(conn, conn_id, options, task, list(result), tlasted)


@celery.task(name="scan.api")
def task_scan(conn, conn_id, task, options, lasted=False, vars=[]):
    access = decodeConn(conn, conn_id, task)

    oVars = Normalize.optionsVarsNormalize(options['vars']),
    vars = sum(oVars, vars)

    try:
        Crawler = FactoryAPI(access=access, conn=conn)
        result = Crawler.execute(options, vars)

        if not result['result']:
            task_last.delay(conn, task, options)
            raise ValueError('Empty result')

        tlasted = lasted and Crawler.isLast()  # lasted of regions and lasted of scan iter
        key = iterTranslate(conn, conn_id, options, task, result['result'], tlasted)

        if Crawler.isLast() == False:
            factoryPag = Crawler.checkPag()
            task_scan.delay(conn, conn_id, task, options, lasted, [factoryPag])

        return {
            'translate-id': str(key),
            'conn_id': conn_id,
            'options': options,
            'qtd': len(result['result'])
        }

    except TypeError as error:
        return {'msg': str(error), 'name': error.__class__.__name__}

    except Exception as error:
        status = 'warning'
        code = 500

        if error.__class__.__name__ == 'ClientMaestroError':
            status = 'danger'
            code = 403

        if lasted:
            task_ws.apply_async((conn, conn_id, task, status), countdown=app.config['MAESTRO_COUNTDOWN_WS'])
            task_last.apply_async((conn, task, options), countdown=app.config['MAESTRO_COUNTDOWN_LAST'])

        task_notification.delay(msg=str(error), conn_id=conn_id, task=task, status=status)

        return FactoryInvalid.responseInvalid(
            {'msg': str(error), 'name': error.__class__.__name__}
            , code
        )
