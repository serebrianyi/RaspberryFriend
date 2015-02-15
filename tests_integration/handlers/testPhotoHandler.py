import unittest
from mock import patch
from util.DateUtil import DateUtil
import os
from tests_integration.TestUtil import TestUtil


class PhotoHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        xmpp_service = TestUtil.get_xmpp_service()
        filename = os.path.join(TestUtil.get_current_directory(__file__), "photos/fake_filename.jpg")
        with patch.object(DateUtil, 'get_current_datetime_as_filename', return_value="fake_filename"):
                xmpp_service.message(TestUtil.get_xmpp_message("photo"))
                xmpp_service.reply.assert_called_once_with(
                    TestUtil.get_xmpp_response("photo"),
                    "An e-mail with photo %s was sent" % filename
                )
                self.assertTrue(os.path.isfile(filename))
