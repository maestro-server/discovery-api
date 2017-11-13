
from flask_restful import Resource
from app.models import Adminer, Providers

from app.error.factoryInvalid import FactoryInvalid
from app.tasks import task_scan
from pydash.objects import pick


class CrawlerApps(Resource):
    def get(self, datacenter, instance, task):
        return {
            'datacenter': datacenter,
            'instance': instance,
            'task': task
        }

    def put(self, datacenter, instance, task):
        require = Adminer().getOptions('providers', len='.permissions.%s.%s' % (datacenter, task))
        if not require:
            return FactoryInvalid.responseInvalid('This task is not allowed')

        return self.crawlerFactory(instance, task, require)


    def crawlerFactory(self, instance, task, require):
        Provider = Providers(instance)
        connector = Provider.get()
        if not connector['conn']:
            return FactoryInvalid.responseInvalid('This instance dont have a valid connection.')


        try:
            for commands in require:
                for region in connector['regions']:

                    conn = {
                        **pick(connector, ['conn', 'provider', 'dc']),
                        **{'region': region}
                    }
                    key = task_scan.delay(conn, str(connector['_id']), task, commands)
                    return str(key)

            return Provider.markWarning(task).updateState('In progress. %s' % key)

        except Exception as error:
            Provider.markWarning(task).updateState(str(error))
            return FactoryInvalid.responseInvalid({'msg': str(error), 'name': error.__class__.__name__}, 500)