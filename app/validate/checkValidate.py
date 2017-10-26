
from flask_restful.reqparse import RequestParser

class checkValidate(object):

    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("conn", type=str, required=True, help="Name has to be valid string")
        valid.add_argument("name", required=True)
        valid.add_argument("require", required=True)

        return valid.parse_args()