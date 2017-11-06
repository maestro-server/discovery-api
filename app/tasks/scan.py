
from app import celery

@celery.task(name="retrive.api", queue="retrive")
def task_scan(x, y):
    return x + y