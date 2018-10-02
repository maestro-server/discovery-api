
import json
from flask_restful import Resource
from pydash.objects import pick

from app.tasks import task_scan, task_notification, task_setup

from app.libs.normalize import Normalize
from app.libs.lens import lens
from app.repository.externalMaestroData import ExternalMaestroData
from app.error.factoryInvalid import FactoryInvalid

import requests
from app.libs.url import FactoryURL


class CrawlerApps(Resource):
    # @api {get} /crawler/<datacenter>/<instance>/<task> 1. Health check
    # @apiName GetCrawlerInstance
    # @apiGroup Crawler

    # @apiSuccessExample {json} Success-Response:
    # HTTP/1.1 200 OK
    # {
    #     'datacenter': <string>,
    #     'instance': <string>,
    #     'task': <string>
    # }
    def get(self, datacenter, instance, task):
        return {
            'datacenter': datacenter,
            'instance': instance,
            'task': task
        }

    # @api {put} /crawler/<datacenter>/<instance>/<task> 2. Execute crawler
    # @apiName PostDatacenterCrawler
    # @apiGroup Crawler
    # @apiDescription Used to run jobs, all jobs execute in workers tasks. All task is process by discovery-worker

    # @apiParam (Query) {String} instance Instance ID of connection.
    # @apiParam (Query) {String} task Task (server-list, db-list)
    # @apiParam (Query) {String} datacenter Datacenter name (AWS, OpenStack)

    # @apiSuccessExample {json} Success-Response:
    # HTTP/1.1 200 OK
    # [{
    #     'name': (string)
    # }]
    def put(self, datacenter, instance, task):
        filters = json.dumps({'key': 'connections'})
        listC = ExternalMaestroData().post_request(path="adminer", body={'query': filters})

        result = json.loads(listC)
        if listC and 'items' in result:
            require = lens(result['items'], len='.permissions.%s.%s' % (datacenter, task))

            if require:
                return self.crawlerFactory(instance, task, require)

        return FactoryInvalid.responseInvalid('This task is not allowed', 422)

    def crawlerFactory(self, instance, task, require):
        print(instance)
        path = FactoryURL.make(path="connections/%s" % instance)
        results = requests.get(path)
        connector = results.json()

        print(connector, instance)
        connector = ExternalMaestroData().get_request(path="connections/%s" % instance)
        print(connector, instance)

        if connector == None:
            return FactoryInvalid.responseInvalid('This instance dont have a valid connection.')

        try:
            for commands in require:
                for region in connector['regions']:
                    task_setup(connector['dc_id'], task, region)

                    conn = {
                        **pick(connector, ['dc_id', 'conn', 'provider', 'dc', 'owner_user', 'url', 'project', 'roles', 'user_domain_id', 'api_version']),
                        **{'region': region}
                    }

                    Normalize.singleKeyObjectIdToStr(conn, 'owner_user._id')
                    Normalize.arrayKeyObjectIdToStr(conn, 'roles', '_id')
                    Normalize.singleKeyObjectIdToStr(connector, '_id')
                    key = task_scan.delay(conn, connector['_id'], task, commands)

            message = {'msg': 'In progress. %s' % key, 'conn_id': instance, 'task': task, 'status': 'warning'}
            task_notification.delay(**message)
            return message, 201

        except Exception as error:
            task_notification.delay(msg=str(error), conn_id=instance, task=task, status='danger')
            return FactoryInvalid.responseInvalid({'msg': str(error), 'name': error.__class__.__name__}, 500)