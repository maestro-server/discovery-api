
from app.validate.aggregateValidate import aggregateValidate
from flask_restful import Resource

class AggregationApp(Resource):
    def post(self):
        valid = aggregateValidate().validate()

        if valid:
