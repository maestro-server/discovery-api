from app.libs.jwt import Jwt
from app.error import FactoryInvalid
from app.tasks.notification import task_notification


def decodeConn(conn, conn_id, task):
    try:
        return Jwt.decode(conn['conn'])
    except Exception as error:
        task_notification.delay(msg=str(error), conn_id=conn_id, task=task, status='danger')
        return FactoryInvalid.responseInvalid(
            {'msg': str(error), 'name': error.__class__.__name__}
            , 403
        )
