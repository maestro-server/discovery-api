from flask_restful.reqparse import RequestParser

class connValidate(object):

    def task_status(self, value):
        statuses = ["danger", "warning", "success"]
        if value in statuses:
            return value

    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("msg", type=str, required=True)
        valid.add_argument("status", required=True, type=self.task_status, help="Use danger, warning or success")
        valid.add_argument("task", required=True)

        return valid.parse_args()