
from flask_restful import Resource
from app.services.factory import FactoryAPI

from app.models import Adminer, Providers
from app.libs.jwt import Jwt

from jwt.exceptions import DecodeError
from app.error.factoryInvalid import FactoryInvalid
from app.error.clientMaestroError import ClientMaestroError
from app.error.missingError import MissingError


class CrawlerApps(Resource):
    def get(self, datacenter, instance, task, type='parcial'):
        return {
            'datacenter': datacenter,
            'type': type,
            'instance': instance,
            'task': task
        }

    def put(self, datacenter, instance, task):
        require = Adminer().getOptions('providers', len='.permissions.%s.%s' % (datacenter, task))
        if not require:
            return FactoryInvalid.responseInvalid('This task is not allowed')

        Provider = Providers(instance)
        conn = Provider.get(len='.conn')
        if not conn:
            return FactoryInvalid.responseInvalid('This instance dont have a valid connection.')

        try:
            access = Jwt.decode(conn)
        except DecodeError as error:
            return FactoryInvalid.responseInvalid(str(error), 403)
        except Exception as error:
            return FactoryInvalid.responseInvalid(str(error), 500)

        return self.crawlerFactory(Provider, task, access, datacenter, require)


    def crawlerFactory(self, Provider, task, access, datacenter, require):
        try:
            success = FactoryAPI(access=access, dc=datacenter).execute(require)

            return Provider.markSucess(task)\
                .updateState('Success crawler, dc %s with regions %s' % (datacenter, ' '.join(access['regions'])))

        except (ClientMaestroError, MissingError) as error:
            Provider.markError(task)\
                .updateState(str(error))

            return FactoryInvalid.responseInvalid({'msg': str(error), 'name': error.__class__.__name__}, 403)

        except Exception as error:
            Provider.markWarning(task) \
                .updateState(str(error))

            return FactoryInvalid.responseInvalid({'msg': str(error), 'name': error.__class__.__name__}, 500)