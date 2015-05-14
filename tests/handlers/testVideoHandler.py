import unittest
from handlers.VideoHandler import VideoHandler
from mock import MagicMock, call



class VideoHandlerTestCase(unittest.TestCase):

    def test_should_process_to_all(self):
        handler = VideoHandler()
        handler._get_mail_service = MagicMock()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual("An e-mail with video test_name was sent", handler.process(5))
        handler._record.assert_called_with("test_name", 5)
        self.assertEqual(handler._get_mail_service.mock_calls, [call(), call().send_to_all('test_name')])

    def test_should_process_to_sender(self):
        handler = VideoHandler()
        handler._get_mail_service = MagicMock()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual("An e-mail with video test_name was sent", handler.process_to_sender("sender", 5))
        handler._record.assert_called_with("test_name", 5)
        self.assertEqual(handler._get_mail_service.mock_calls, [call(), call().send('sender', 'test_name')])

