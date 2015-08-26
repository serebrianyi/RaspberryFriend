import unittest

from mock import patch
from util.DateUtil import DateUtil
from tests_integration.util.TestUtil import TestUtil


class StatusHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        telegram_service = TestUtil.get_telegram_service()
        with patch.object(DateUtil, 'get_current_datetime_as_string', return_value="01.01.2015 12:13:14"):
            telegram_service.check_updates(TestUtil.get_telegram_message("status"))
            telegram_service.send_text.assert_called_once_with(
                TestUtil.get_telegram_authorized_user(),
                "RaspberryPi is on. Current time: 01.01.2015 12:13:14"
            )
