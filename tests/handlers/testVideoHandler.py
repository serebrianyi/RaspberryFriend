import unittest
from RaspberryFriend.handlers.VideoHandler import VideoHandler
from mock import MagicMock



class VideoHandlerTestCase(unittest.TestCase):

    def test_should_process_to_all(self):
        handler = VideoHandler()
        handler._send_mail_to_all = MagicMock()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual("An e-mail with video test_name was sent", handler.process(5))
        handler._record.assert_called_with("test_name", 5)
        handler._send_mail_to_all.assert_called_with("test_name")

    def test_should_process_to_sender(self):
        handler = VideoHandler()
        handler._send_mail_to_sender = MagicMock()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual("An e-mail with video test_name was sent", handler.process_to_sender("sender", 5))
        handler._record.assert_called_with("test_name", 5)
        handler._send_mail_to_sender.assert_called_with("sender", "test_name")

