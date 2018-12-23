
from app import celery
from pydash.objects import omit
from .external_audit import task_external_audit

@celery.task(name="audit.api")
def task_audit(entity, lindex, result):

    for iindex in lindex:
        index = iindex.get('index')

        result[index].update({
            '_id': iindex.get('_id'),
            'mkt_created': True
        })

    for obj in result:

        tmp = omit(obj, ['_id', 'mkt_created'])
        path = "audit/%s/%s" % (entity, obj.get('_id'))
        method = "post" if obj.get('mkt_created') else "put"

        task_external_audit.delay(path, tmp, method)

    return {'entity': entity}