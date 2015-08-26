import unittest
import os

from mock import patch
from util.DateUtil import DateUtil
from tests_integration.util.TestUtil import TestUtil


class PhotoHandlerITCase(unittest.TestCase):

    def test_should_process(self):
        telegram_service = TestUtil.get_telegram_service()
        filename = os.path.join(TestUtil.get_current_directory(__file__), "photos/fake_filename.jpg")
        with patch.object(DateUtil, 'get_current_datetime_as_filename', return_value="fake_filename"):
                telegram_service.check_updates(TestUtil.get_telegram_message("photo"))
                telegram_service.send_photo.assert_called_once_with(
                    TestUtil.get_telegram_authorized_user(),
                    filename
                )
                self.assertTrue(os.path.isfile(filename))
