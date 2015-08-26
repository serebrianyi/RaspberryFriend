import unittest

from tests_integration.util.TestUtil import TestUtil


class TempHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        telegram_service = TestUtil.get_telegram_service()
        telegram_service.check_updates(TestUtil.get_telegram_message("temp"))
        mock_call = telegram_service.send_text.mock_calls
        self.assertTrue("Temp" in str(mock_call[0][1]))


