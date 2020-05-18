import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')

DYNAMO_DB_DEBUG = os.environ.get('DYNAMO_DB_DEBUG', 'true')
DYNAMO_DB_REGION_NAME = os.environ.get('DYNAMO_DB_REGION_NAME', 'us-east-1')
DYNAMO_DB_TABLE = os.environ.get('DYNAMO_DB_TABLE', 'pix')
