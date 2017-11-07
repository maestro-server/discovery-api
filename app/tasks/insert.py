
from app import celery
from app.services.factory import FactoryAPI
from app.models import Providers

from app.libs.jwt import Jwt
from jwt.exceptions import DecodeError

from app.error import FactoryInvalid, ClientMaestroError, MissingError


@celery.task(name="scan.api", queue="scan")
def task_scan(task, connector, region, commands, filter=[], pagination=[]):
    try:
        access = Jwt.decode(connector['conn'])
    except DecodeError as error:
        return FactoryInvalid.responseInvalid(str(error), 403)
    except Exception as error:
        return FactoryInvalid.responseInvalid(str(error), 500)


    Provider = Providers(connector['_id'])
    try:
        FactoryAPI(access=access, dc=connector['provider'], region=region).execute(commands)
        return Provider.markSucess(task).updateState('Crawler Success')

    except (ClientMaestroError, MissingError) as error:
        Provider.markError(task).updateState(str(error))
        return FactoryInvalid.responseInvalid({'msg': str(error), 'name': error.__class__.__name__}, 403)

    except Exception as error:
        Provider.markWarning(task).updateState(str(error))
        return FactoryInvalid.responseInvalid({'msg': str(error), 'name': error.__class__.__name__}, 500)

