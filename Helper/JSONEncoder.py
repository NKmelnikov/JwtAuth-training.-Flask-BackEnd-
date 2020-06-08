import json, datetime, time
from bson import ObjectId, datetime


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return {'$oid': str(o)}
        elif isinstance(o, datetime.datetime):
            return {'$date': int(o.timestamp()) * 1000}
        return json.JSONEncoder.default(self, o)
# TODO save the $oid and $date
