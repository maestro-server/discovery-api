import datetime
import json
from bson import ObjectId, timestamp


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, ObjectId) or isinstance(obj, timestamp.Timestamp):
            return str(obj)

        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()

        if isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()

        if isinstance(obj, list):
            return obj.serialize()

        return json.JSONEncoder.default(self, obj)
