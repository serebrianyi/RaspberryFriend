import unittest
from mock import patch
from util.DateUtil import DateUtil
from tests_integration.util.TestUtil import TestUtil

class TramHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        telegram_service = TestUtil.get_telegram_service()
        with patch.object(DateUtil, 'get_current_time', return_value="1423405140"):
                telegram_service.check_updates(TestUtil.get_telegram_message("tram"))
                telegram_service.send_text.assert_called_once_with(
                    TestUtil.get_telegram_authorized_user(),
                    "Leave at 3:24pm (11,2 - wait for 3 min)"
                )

