
import json
from app.validate.aggregateValidate import aggregateValidate
from flask_restful import Resource
from app.repository import Aggregate

from pydash import map_values_deep, has
from app.libs.deepUpdateForMongo import updaterIds
from app.error.factoryInvalid import FactoryInvalid
from app.error.missingError import MissingError

class AggregationApp(Resource):

    def post(self):
        valid = aggregateValidate().validate()

        if valid:
            try :
                pipeline = json.loads(valid['pipeline'])
                entity = valid['entity']
            except Exception as error:    
                return FactoryInvalid.responseInvalid('Invalid Pipeline'), 422
            
            if not has(pipeline, '[0].$match.roles\._id'):
                return MissingError('id', 'Must delimite $match which roles._id ($match {role.id})'), 422

            args = map_values_deep(pipeline, updaterIds)

            return {
                'items': Aggregate(entity).pipeline(args)
            }