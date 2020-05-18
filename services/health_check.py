from business.health_check import HealthCheck
from configurations.log import get_logger
from factory import create_application
from utils.response import Response
from utils.response_builder import ResponseBuilder

application = create_application()

logger = get_logger('services.health_check')


@application.get('/')
def health_check():
    try:
        result = HealthCheck.version()
        return Response(200).body(ResponseBuilder.success(result)).build()
    except Exception as e:
        logger.exception(e)
        return Response(500).body(ResponseBuilder.error(e)).build()
