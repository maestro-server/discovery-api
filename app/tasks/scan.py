
from app import celery

@celery.task(name="scan.api", queue="scan")
def task_scan(conn, region):
    return x + y