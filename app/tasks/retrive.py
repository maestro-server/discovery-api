
from app import celery

@celery.task(name="retrive.api", queue="retrive")
def add(x, y):
    return x + y