import boto3
import decimal
import helpers.message as m
import helpers.system_variable as sv
import json


class DecimalEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        if isinstance(o, set):
            p = []
            for s in o:
                p.append(int(s))
            return p
        return super(DecimalEncoder, self).default(o)


class DynamoDB(DecimalEncoder):

    def __init__(self):
        _configuration = DynamoDBResourceConfiguration().get_resource()
        self._resource = boto3.resource(**_configuration)
        self._table = sv.DYNAMO_DB_TABLE

    def get_item_by_key(self, key):
        if type(key) != dict:
            raise Exception(m.INVALID_DATA_TYPE)
        return self.get_table().get_item(self._table, Key=key)

    def get_table(self):
        return self._resource.Table(self._table)

    @staticmethod
    def json_dumps_loads(data):
        _content_json = json.dumps(data, cls=DecimalEncoder, indent=4)
        return json.loads(_content_json)

    def put_item(self, item):
        if type(item) != dict:
            raise Exception(m.INVALID_DATA_TYPE)
        self.get_table().put_item(Item=item)


class DynamoDBResourceConfiguration:

    def __init__(self):
        self._debug = str(sv.DYNAMO_DB_DEBUG).lower() == 'true'

    @staticmethod
    def get_debug_configuration():
        return {
            'aws_access_key_id': sv.AWS_ACCESS_KEY_ID,
            'aws_secret_access_key': sv.AWS_SECRET_ACCESS_KEY,
            'region_name': sv.DYNAMO_DB_REGION_NAME,
            'service_name': 'dynamodb'
        }

    @staticmethod
    def get_default_configuration():
        return {
            'region_name': sv.DYNAMO_DB_REGION_NAME,
            'service_name': 'dynamodb'
        }

    def get_resource(self):
        return self.select_configuration()

    def select_configuration(self):
        if self._debug:
            return self.get_debug_configuration()
        return self.get_default_configuration()
