from configurations.log import get_logger
from helpers.dynamodb import DynamoDB
from utils.response import Response

import pydash as _
import uuid

logger = get_logger('business.pix')


class PixBusiness:

    @staticmethod
    def create(data):
        try:
            _id = uuid.uuid4().__str__()
            _item = {
                'id': _id,
                'id_transacao': _.get(data, 'id_transacao')
                if _.get(data, 'id_transacao') is not None or _.get(data, 'id_transacao') != ''
                else _id,
                'valor': _.get(data, 'valor')
            }
            DynamoDB().put_item(_item)
            return _item
        except Exception as e:
            logger.exception(e)
            return Response(500).raise_request()
