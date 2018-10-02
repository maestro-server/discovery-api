from app.libs.logger import logger
from app.libs.statusCode import string_status
from app.tasks.notification import task_notification


def notify_error(task, owner_id, graph_id, msg, status="error"):
    msg = '[%s] %s' % (task, msg)
    notification_id = task_notification(graph_id=graph_id, owner_id=owner_id, msg=msg, status=status)
    logger.error(msg)
    return string_status(task, notification_id)