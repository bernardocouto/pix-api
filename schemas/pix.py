from bottle_cerberus import Schema
from schemas.validator import Validator


class PixSchema(Schema, Validator):

    @staticmethod
    def schema():
        return {
            'valor': {
                'min': 0,
                'required': False,
                'type': 'float'
            }
        }
