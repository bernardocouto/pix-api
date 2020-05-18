class ResponseBuilder:

    @staticmethod
    def error(message):
        return {
            'data': None,
            'error': True,
            'message': message,
            'success': False
        }

    @staticmethod
    def success(data):
        return {
            'data': data,
            'error': False,
            'message': None,
            'success': True
        }
