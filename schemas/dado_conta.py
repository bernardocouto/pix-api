from bottle_cerberus import Schema
from schemas.validator import Validator


class DadosContaSchema(Schema, Validator):

    @staticmethod
    def schema():
        return {
            'agencia': {
                'required': False,
                'type': 'string'
            },
            'banco': {
                'required': False,
                'type': 'string'
            },
            'conta': {
                'required': False,
                'type': 'string'
            }
        }
