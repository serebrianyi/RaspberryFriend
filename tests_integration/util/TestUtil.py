from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum
from domain_services.telegram_service.TelegramService import TelegramService
from mock import MagicMock
import os

class TestUtil(object):

    @staticmethod
    def get_telegram_authorized_user():
        configuration_telegram = Configuration()
        configuration_telegram.load(ConfigurationEnum.Telegram)
        return configuration_telegram.allowed_access[0]

    @staticmethod
    def get_telegram_message(body):
        return [{"update_id":32, "message":{"message_id":66,"from":{"id":TestUtil.get_telegram_authorized_user(),"first_name":"34"},"chat":{"id":TestUtil.get_telegram_authorized_user(),"first_name":"33"},"text":body}}]

    @staticmethod
    def get_telegram_response(body):
        return {'body': body, 'type': 'chat', 'from': TestUtil.get_telegram_authorized_user()}

    @staticmethod
    def get_telegram_service():
        configuration_telegram = Configuration()
        configuration_telegram.load(ConfigurationEnum.Telegram)
        telegram_service = TelegramService(configuration_telegram)
        telegram_service.send_video = MagicMock(return_value=None)
        telegram_service.send_photo = MagicMock(return_value=None)
        telegram_service.send_text = MagicMock(return_value=None)
        return telegram_service

    @staticmethod
    def get_current_directory(file):
        return os.path.dirname(file).replace("tests_integration%s" % os.path.sep, "")