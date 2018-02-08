from flask_restful.reqparse import RequestParser

class aggregateValidate(object):


    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("pipeline", required=True)
        valid.add_argument("entity", required=True)

        return valid.parse_args()