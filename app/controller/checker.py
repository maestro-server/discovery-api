
from flask_restful import Resource
from app.validate.checkValidate import checkValidate

from app.services.jwt import Jwt
from app.services.factory import FactoryAPI
from pydash.objects import defaults

class CheckerApp(Resource):

    def put(self, datacenter):
        valid = checkValidate().validate()
        access = Jwt.decode(valid.conn)

        checker = FactoryAPI(access=access, dc=valid.name).check(valid.require)

        print(checker)

        if 'error' in checker:
            defaults(checker, {'status': 400})
            return checker, checker['status']

        return checker