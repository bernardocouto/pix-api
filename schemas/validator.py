import cerberus


class Validator:

    @staticmethod
    def validate(schema, data):
        validator = cerberus.Validator(schema)
        if not validator.validate(data):
            raise ValueError(f'{validator.errors}')
        return True
