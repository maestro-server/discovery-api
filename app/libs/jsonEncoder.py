
import datetime
import json
from bson import ObjectId


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        if attr.has(val.__class__):
            return attr.asdict(val)       
        if isinstance(val, Exception):
            return {
            "error": val.__class__.__name__,
            "args": val.args,
        }
        
        return json.JSONEncoder.default(self, obj)