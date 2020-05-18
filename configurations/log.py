import logging
import logging.config
import os

logger = {}


class Log:

    def __init__(self):
        self._directory = os.path.abspath(os.path.dirname(__file__))
        self._file = os.path.join(self._directory, 'log.ini')

    def configuration(self):
        self.ignored_module()
        logging.config.fileConfig(self._file)

    @staticmethod
    def get_instance(module):
        global logger
        if module not in logger:
            logger[module] = logging.getLogger(module)
        return logger[module]

    @staticmethod
    def ignored_module():
        modules = [
            'boto3'
        ]
        for module in modules:
            logging.getLogger(module).setLevel(logging.WARNING)


log = Log()
log.configuration()


def get_logger(module='sdc'):
    return log.get_instance(module)
