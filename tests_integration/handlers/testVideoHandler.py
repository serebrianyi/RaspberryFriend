import unittest
from mock import patch
from RaspberryFriend.util.DateUtil import DateUtil
import os
from RaspberryFriend.tests_integration.TestUtil import TestUtil


class VideoHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        xmpp_service = TestUtil.get_xmpp_service()
        filename = os.path.join(TestUtil.get_current_directory(__file__), "videos/fake_filename.h264")
        with patch.object(DateUtil, 'get_current_datetime_as_filename', return_value="fake_filename"):
                xmpp_service.message(TestUtil.get_xmpp_message("video"))
                xmpp_service.reply.assert_called_once_with(
                    TestUtil.get_xmpp_response("video"),
                    "An e-mail with video %s was sent" % filename
                )
                self.assertTrue(os.path.isfile(filename))

    def test_should_process_with_specific_time_value(self):
        xmpp_service = TestUtil.get_xmpp_service()
        filename = os.path.join(TestUtil.get_current_directory(__file__), "videos/fake_filename.h264")
        with patch.object(DateUtil, 'get_current_datetime_as_filename', return_value="fake_filename"):
                xmpp_service.message(TestUtil.get_xmpp_message("video 3"))
                xmpp_service.reply.assert_called_once_with(
                    TestUtil.get_xmpp_response("video 3"),
                    "An e-mail with video %s was sent" % filename
                )
                self.assertTrue(os.path.isfile(filename))
