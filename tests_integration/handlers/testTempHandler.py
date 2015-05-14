import unittest

from tests_integration.util.TestUtil import TestUtil


class TempHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        xmpp_service = TestUtil.get_xmpp_service()
        xmpp_service.message(TestUtil.get_xmpp_message("temp"))
        mock_call = xmpp_service.reply.mock_calls
        self.assertTrue("Temp" in str(mock_call[0][1]))

