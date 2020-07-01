from app import celery
from app.repository.externalMaestroAudit import ExternalMaestroAudit


@celery.task(name="external_audit.api")
def task_external_audit(path, tmp, method="post"):
    rfunction = "%s_request" % method

    try:
        ExternalAudit = ExternalMaestroAudit()
        getattr(ExternalAudit, rfunction)(path=path, body=tmp)
        ExternalAudit.get_raw()

    except Exception as error:
        return {'message': str(error)}

    return {'api': path}
