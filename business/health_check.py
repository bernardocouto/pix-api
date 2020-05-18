from configurations.log import get_logger
from utils.version import version

logger = get_logger('business.health_check')


class HealthCheck:

    @staticmethod
    def version():
        try:
            return {
                'version': version.__str__()
            }
        except Exception as e:
            logger.exception(e)
