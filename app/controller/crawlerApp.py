
from flask_restful import Resource
from pydash.objects import pick

from app.services.privateAuth import private_auth
from app.tasks import task_ws, task_scan, task_notification, task_setup

from app.libs.normalize import Normalize
from app.repository.externalMaestroData import ExternalMaestroData
from app.error.factoryInvalid import FactoryInvalid
from app.libs.providersRules import providersRules


class CrawlerApps(Resource):
    @private_auth
    def get(self, datacenter, instance, task):
        """
        @api {get} /crawler/<datacenter>/<instance>/<task> 1. Health check
        @apiName GetCrawlerInstance
        @apiGroup Crawler

        @apiParam (Param) {String} [datacenter] datacenter provider.
        @apiParam (Param) {String} [task] Name task [server-list, loadbalance-list, storage-list].

        @apiPermission JWT Private (MAESTRO_SECRETJWT_PRIVATE)
        @apiHeader (Header) {String} Authorization JWT {Token}

        @apiError (Error) PermissionError Token don`t have permission
        @apiError (Error) Unauthorized Invalid Token

        @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            'datacenter': <string>,
            'instance': <string>,
            'task': <string>
        }
        """
        return {
            'datacenter': datacenter,
            'instance': instance,
            'task': task
        }

    @private_auth
    def put(self, datacenter, instance, task):
        """
        @api {put} /crawler/<datacenter>/<instance>/<task> 2. Execute crawler
        @apiName PostDatacenterCrawler
        @apiGroup Crawler
        @apiDescription Used to run jobs, all jobs execute in workers tasks. All task is process by discovery-worker

        @apiParam (Query) {String} instance Instance ID of connection.
        @apiParam (Query) {String} task Task (server-list, db-list)
        @apiParam (Query) {String} datacenter Datacenter name (AWS, OpenStack)

        @apiPermission JWT Private (MAESTRO_SECRETJWT_PRIVATE)
        @apiHeader (Header) {String} Authorization JWT {Token}

        @apiError (Error) PermissionError Token don`t have permission
        @apiError (Error) Unauthorized Invalid Token

        @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        [{
            'name': (string)
        }]
        """

        result = providersRules(datacenter)
        require = result.get('permissions', {}).get(task)

        if require:
            return self.crawlerFactory(instance, task, require)

        return FactoryInvalid.responseInvalid('This task is not allowed', 422)


    def crawlerFactory(self, instance, task, require):
        connector = ExternalMaestroData()\
                        .list_request(path="connections/%s" % instance)\
                        .get_results()

        if connector == None:
            return FactoryInvalid.responseInvalid('This instance dont have a valid connection.')

        try:

            lastp = (len(require)-1, len(connector['regions'])-1)
            for ireq, commands in enumerate(require):
                for iregion, region in enumerate(connector['regions']):
                    lasted = lastp[0] == ireq and lastp[1] == iregion

                    task_setup(connector['dc_id'], task, connector['_id'], region)
                    self.spawnScan(connector, region, task, commands, lasted)

        except Exception as error:
            task_ws.delay(connector, connector['_id'], task, 'danger')
            task_notification.delay(msg=str(error), conn_id=instance, task=task, status='danger')
            return FactoryInvalid.responseInvalid({'msg': str(error), 'name': error.__class__.__name__}, 500)

        else:
            message = {'msg': 'In progress. %s' % task, 'conn_id': instance, 'task': task, 'status': 'warning'}
            task_notification.delay(**message)
            return message, 201


    def spawnScan(self, connector, region, task, commands, lasted):
        conn = {
            **pick(connector,
                   ['dc_id', 'conn', 'provider', 'service', 'dc', 'owner_user', 'url', 'project', 'roles', 'user_domain_id',
                    'api_version', '_id']),
            **{'region': region}
        }

        Normalize.singleKeyObjectIdToStr(conn, 'owner_user._id')
        Normalize.arrayKeyObjectIdToStr(conn, 'roles', '_id')
        Normalize.singleKeyObjectIdToStr(connector, '_id')
        task_scan.delay(conn, connector['_id'], task, commands, lasted)