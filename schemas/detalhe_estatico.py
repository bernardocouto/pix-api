from bottle_cerberus import Schema
from schemas.validator import Validator


class DetalheEstaticoSchema(Schema, Validator):

    @staticmethod
    def schema():
        return {
            'mensagem': {
                'required': False,
                'type': 'string'
            }
        }
