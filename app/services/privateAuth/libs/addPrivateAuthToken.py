from app.libs.appInfo import appInfo
from app.services.privateAuth.auth import PrivateAuth


def create_token():
    info = appInfo()
    return PrivateAuth.create_token(info)
