import unittest
from tests_integration.util.TestUtil import TestUtil
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class QuoteHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        xmpp_service = TestUtil.get_xmpp_service()
        xmpp_service.message(TestUtil.get_xmpp_message("quotes"))
        mock_call = xmpp_service.reply.mock_calls
        response = str(mock_call[0][1])
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Quote)
        for quote in configuration.quotes:
            self.assertTrue(quote in response)