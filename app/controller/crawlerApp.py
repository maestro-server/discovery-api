
from flask_restful import Resource
from app.error.factoryInvalid import FactoryInvalid
from app.models import Adminer, Providers
from app.services.jwt import Jwt
from jwt.exceptions import DecodeError

from app.services.factory import FactoryAPI

class CrawlerApps(Resource):
    def get(self, datacenter, instance, task, type='parcial'):
        return {
            'datacenter': datacenter,
            'type': type,
            'instance': instance,
            'task': task
        }

    def put(self, datacenter, instance, task, type='parcial'):
        require = Adminer().getOptions('providers', len='.permissions.%s.%s' % (datacenter, task))
        if not require:
            return FactoryInvalid.responseInvalid('This task is not allowed')

        conn = Providers().get(instance, len='.conn')
        if not conn:
            return FactoryInvalid.responseInvalid('This instance dont have a valid connection.')

        try:
            access = Jwt.decode(conn)
        except DecodeError as error:
            return FactoryInvalid.responseInvalid(str(error), 403)
        except Exception as error:
            return FactoryInvalid.responseInvalid(str(error), 500)

        try:
            success = FactoryAPI(access=access, dc=datacenter).execute(require)
        except Exception as error:
            return FactoryInvalid.responseInvalid(str(error), 403)



        return success