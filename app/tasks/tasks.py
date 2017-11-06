
from app import celery

@celery.task(name="tasks.add", queue="add")
def add(x, y):
    return x + y