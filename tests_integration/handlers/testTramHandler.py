import unittest
from mock import patch
from util.DateUtil import DateUtil
from tests_integration.util.TestUtil import TestUtil

class TramHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        xmpp_service = TestUtil.get_xmpp_service()
        with patch.object(DateUtil, 'get_current_time', return_value="1423405140"):
                xmpp_service.message(TestUtil.get_xmpp_message("tram"))
                xmpp_service.reply.assert_called_once_with(
                    TestUtil.get_xmpp_response("tram"),
                    "Leave at 3:24pm (11,8 - wait for 4 min)"
                )

