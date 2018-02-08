from flask_restful.reqparse import RequestParser

class aggregateValidate(object):


    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("msg", type=str, required=True)
        valid.add_argument("task", required=True)

        return valid.parse_args()