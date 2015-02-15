import unittest
from RaspberryFriend.handlers.PhotoHandler import PhotoHandler
from mock import MagicMock


class PhotoHandlerTestCase(unittest.TestCase):

    def test_should_process_to_all(self):
        handler = PhotoHandler()
        handler._send_mail_to_all = MagicMock()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual("An e-mail with photo test_name was sent", handler.process())
        handler._record.assert_called_once_with("test_name")
        handler._send_mail_to_all.assert_called_once_with("test_name")

    def test_should_process_to_sender(self):
        handler = PhotoHandler()
        handler._send_mail_to_sender = MagicMock()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual("An e-mail with photo test_name was sent", handler.process_to_sender("sender"))
        handler._record.assert_called_once_with("test_name")
        handler._send_mail_to_sender.assert_called_once_with("sender", "test_name")