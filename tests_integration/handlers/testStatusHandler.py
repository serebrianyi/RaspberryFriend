import unittest
from mock import patch
from util.DateUtil import DateUtil
from tests_integration.TestUtil import TestUtil


class StatusHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        xmpp_service = TestUtil.get_xmpp_service()
        with patch.object(DateUtil, 'get_current_datetime_as_string', return_value="01.01.2015 12:13:14"):
            xmpp_service.message(TestUtil.get_xmpp_message("status"))
            xmpp_service.reply.assert_called_once_with(
                TestUtil.get_xmpp_response("status"),
                "RaspberryPi is on. Current time: 01.01.2015 12:13:14"
            )
