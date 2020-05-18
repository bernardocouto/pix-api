from bottle import request
from business.pix import PixBusiness
from configurations.log import get_logger
from factory import create_application
from schemas.pix import PixSchema
from utils.response import Response
from utils.response_builder import ResponseBuilder

application = create_application()

logger = get_logger('services.pix')


@application.post('/pix')
def create():
    try:
        _data = dict(request.json)
        PixSchema().validate(PixSchema().schema(), _data)
        result = PixBusiness().create(_data)
        return Response(201).body(result).build()
    except Exception as e:
        logger.exception(e)
        return Response(500).body(ResponseBuilder.error(e)).build()
