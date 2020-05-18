from bottle_cerberus import Schema
from schemas.validator import Validator


class RecebedorSchema(Schema, Validator):

    @staticmethod
    def schema():
        return {
            'alias': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'email': {
                'required': False,
                'type': 'string'
            },
            'nome': {
                'maxlength': 200,
                'required': False,
                'type': 'string'
            },
            'telefone': {
                'required': False,
                'type': 'string'
            }
        }
