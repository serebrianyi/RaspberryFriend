import unittest
from tests_integration.util.TestUtil import TestUtil
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class QuoteHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        telegram_service = TestUtil.get_telegram_service()
        telegram_service.check_updates(TestUtil.get_telegram_message("quotes"))
        mock_call = telegram_service.send_text.mock_calls
        response = str(mock_call[0][1])
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Quote)
        for quote in configuration.quotes:
            self.assertTrue(quote in response)