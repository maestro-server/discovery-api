
from app.libs.appInfo import appInfo
from app.services.privateAuth.auth import PrivateAuth

def createToken():

    info = appInfo()
    return PrivateAuth.create_token(info)