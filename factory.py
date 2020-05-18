from bottle import Bottle, JSONPlugin

import datetime
import decimal
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.isoformat()
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        if isinstance(o, decimal.Decimal):
            return float(o)
        return json.JSONEncoder.default(self, o)


def create_application():
    application = Bottle()
    application.install(JSONPlugin(json_dumps=lambda o: json.dumps(o, cls=JSONEncoder)))
    return application
