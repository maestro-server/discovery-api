
import datetime
import json
from bson import ObjectId, timestamp

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()
        if isinstance(obj, timestamp.Timestamp):
            return str(obj)
        if isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()


        return json.JSONEncoder.default(self, obj)