
import datetime
import json
from bson import ObjectId, timestamp


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        val = None

        if isinstance(obj, ObjectId) or isinstance(obj, timestamp.Timestamp):
            val = str(obj)

        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            val = obj.isoformat()

        if isinstance(obj, datetime.timedelta):
            val = (datetime.datetime.min + obj).time().isoformat()

        if val is None:
            val = json.JSONEncoder.default(self, obj)

        return val