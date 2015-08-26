import unittest
from configuration.Configuration import Configuration
from mock import MagicMock
import sys
sys.modules['domain_services.logging_service.LoggingService'] = MagicMock()
from domain_services.telegram_service.TelegramService import TelegramService


class TelegramServiceTestCase(unittest.TestCase):

    def test_should_not_allow_unauthorized(self):
        configuration = Configuration()
        configuration.name = "name"
        configuration.password = "password"
        configuration.is_master = True
        configuration.allowed_access = [111, 2222]
        telegram_service = TelegramService(configuration)
        telegram_service.send_text = MagicMock(return_value=None)
        msg = [{"update_id":32, "message":{"message_id":66,"from":{"id":333,"first_name":"34"},"chat":{"id":333,"first_name":"33"},"text":"status"}}]
        telegram_service.check_updates(msg)
        telegram_service.send_text.assert_called_once_with(333, "Unauthorized access from 333")

    def test_should_process_command(self):
        configuration = Configuration()
        configuration.name = "name"
        configuration.password = "password"
        configuration.is_master = True
        configuration.allowed_access = [111, 222]
        telegram_service = TelegramService(configuration)
        telegram_service.send_text = MagicMock(return_value=None)
        msg = [{"update_id":32, "message":{"message_id":66,"from":{"id":111,"first_name":"34"},"chat":{"id":111,"first_name":"33"},"text":"status"}}]
        telegram_service.check_updates(msg)
        self.assertEqual(1, telegram_service.send_text.call_count)


    def test_should_process_command_when_recipient_is_me(self):
        configuration = Configuration()
        configuration.name = "name"
        configuration.password = "password"
        configuration.is_master = False
        configuration.pi_name = "slave"
        configuration.allowed_access = [111, 222]
        telegram_service = TelegramService(configuration)
        telegram_service.send_text = MagicMock(return_value=None)
        msg = [{"update_id":32, "message":{"message_id":66,"from":{"id":111,"first_name":"34"},"chat":{"id":111,"first_name":"33"},"text":"slave status"}}]
        telegram_service.check_updates(msg)
        self.assertEqual(1, telegram_service.send_text.call_count)

    def test_should_not_process_command_when_no_recipient_and_im_not_master(self):
        configuration = Configuration()
        configuration.name = "name"
        configuration.password = "password"
        configuration.is_master = False
        configuration.pi_name = "slave"
        configuration.allowed_access = [111, 222]
        telegram_service = TelegramService(configuration)
        telegram_service.send_text = MagicMock(return_value=None)
        msg = [{"update_id":32, "message":{"message_id":66,"from":{"id":111,"first_name":"34"},"chat":{"id":111,"first_name":"33"},"text":"status"}}]
        telegram_service.check_updates(msg)
        self.assertEqual(0, telegram_service.send_text.call_count)

    def test_should_not_process_command_when_recipient_is_not_me_and_im_not_master(self):
        configuration = Configuration()
        configuration.name = "name"
        configuration.password = "password"
        configuration.is_master = False
        configuration.pi_name = "slave"
        configuration.allowed_access = [111, 222]
        telegram_service = TelegramService(configuration)
        telegram_service.send_text = MagicMock(return_value=None)
        msg = [{"update_id":32, "message":{"message_id":66,"from":{"id":111,"first_name":"34"},"chat":{"id":111,"first_name":"33"},"text":"master status"}}]
        telegram_service.check_updates(msg)
        self.assertEqual(0, telegram_service.send_text.call_count)