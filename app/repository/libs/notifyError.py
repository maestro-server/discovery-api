from app.libs.logger import logger
from app.repository.libs.statusCode import string_status
from app.tasks.notification import task_notification


def notify_error(task, conn_id, msg, status="error"):
    msg = '[%s] %s' % (task, msg)
    notification_id = task_notification(conn_id=conn_id, msg=msg, task=task, status=status)
    logger.error(msg)
    return string_status(task, notification_id)