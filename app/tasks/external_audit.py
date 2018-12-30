
from app import celery
from app.repository.externalMaestroAudit import ExternalMaestroAudit

@celery.task(name="external_audit.api")
def task_external_audit(path, tmp, method="post"):

    rfunction = "%s_request" % method


    try:
        ExternalAudit = ExternalMaestroAudit()
        getattr(ExternalAudit, rfunction)(path=path, body=tmp)

    except Exception as error:
        return {'message': str(error)}

    result = ExternalAudit.get_results()
    return {'api': result}