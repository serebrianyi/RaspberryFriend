import unittest
from handlers.PhotoHandler import PhotoHandler
from mock import MagicMock, call


class PhotoHandlerTestCase(unittest.TestCase):

    def test_should_process_to_all(self):
        handler = PhotoHandler()
        handler._get_mail_service = MagicMock()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual("An e-mail with photo test_name was sent", handler.process())
        handler._record.assert_called_once_with("test_name")
        self.assertEqual(handler._get_mail_service.mock_calls, [call(), call().send_to_all('test_name')])

    def test_should_process_to_sender(self):
        handler = PhotoHandler()
        handler._get_mail_service = MagicMock()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual("An e-mail with photo test_name was sent", handler.process_to_sender("sender"))
        handler._record.assert_called_once_with("test_name")
        self.assertEqual(handler._get_mail_service.mock_calls, [call(), call().send('sender', 'test_name')])

