
from flask_restful import Resource
from app.repository import Adminer, Connections

from app.error.factoryInvalid import FactoryInvalid
from app.tasks import task_scan
from pydash.objects import pick

from app.libs.normalize import Normalize


class CrawlerApps(Resource):
    """
    @api {get} /crawler/<datacenter>/<instance>/<task> 1. Health check
    @apiName GetCrawlerInstance
    @apiGroup Crawler

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        'datacenter': <string>,
        'instance': <string>,
        'task': <string>
    }
    """

    def get(self, datacenter, instance, task):
        return {
            'datacenter': datacenter,
            'instance': instance,
            'task': task
        }

    """
    @api {post} /crawler/<datacenter> 2. Execute crawler
    @apiName PostDatacenterCrawler
    @apiGroup Crawler
    @apiDescription Used to run jobs, all jobs execute in workers tasks.

    @apiParam (Query) {String} instance Instance ID of connection.
    @apiParam (Query) {String} task Task
    @apiParam (Query) {String} datacenter Datacenter name

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    [{
        'name': (string)
    }]
    """
    def put(self, datacenter, instance, task):
        require = Adminer().getOptions('connections', len='.permissions.%s.%s' % (datacenter, task))
        if not require:
            return FactoryInvalid.responseInvalid('This task is not allowed')

        return self.crawlerFactory(instance, task, require)


    def crawlerFactory(self, instance, task, require):
        Connection = Connections(instance)
        connector = Connection.get()
        if not connector and connector['conn']:
            return FactoryInvalid.responseInvalid('This instance dont have a valid connection.')


        try:
            for commands in require:
                for region in connector['regions']:

                    conn = {
                        **pick(connector, ['dc_id', 'conn', 'provider', 'dc', 'owner_user', 'url', 'project', 'roles']),
                        **{'region': region}
                    }

                    Normalize.singleKeyObjectIdToStr(conn, 'owner_user._id')
                    Normalize.arrayKeyObjectIdToStr(conn, 'roles', '_id')
                    Normalize.singleKeyObjectIdToStr(connector, '_id')
                    key = task_scan.delay(conn, connector['_id'], task, commands)

            return Connection.markWarning(task).updateState('In progress. %s' % key)

        except Exception as error:
            Connection.markWarning(task).updateState(str(error))
            return FactoryInvalid.responseInvalid({'msg': str(error), 'name': error.__class__.__name__}, 500)