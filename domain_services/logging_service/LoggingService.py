import logging
import logging.config
import os


class LoggingService(object):

    logging.config.fileConfig(os.path.join(os.path.dirname(__file__), 'logging.conf'), None, False)
    logger = logging.getLogger(__name__)

    @classmethod
    def error(cls, error_message):
        cls.logger.error(error_message)

    @classmethod
    def exception(cls, exception):
        cls.logger.exception(exception)

    @classmethod
    def info(cls, info_message):
        cls.logger.info(info_message)
