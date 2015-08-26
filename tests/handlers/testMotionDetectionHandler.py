import unittest
import sys
from mock import MagicMock
from configuration.Configuration import Configuration
from datetime import datetime, timedelta
sys.modules['domain_services.logging_service.LoggingService'] = MagicMock()
from handlers.MotionDetectionHandler import MotionDetectionHandler


class MotionDetectionHandlerTestCase(unittest.TestCase):

    def test_someone_should_be_home(self):
        configuration = Configuration()
        configuration.ip = ["123", "234"]
        handler = MotionDetectionHandler(configuration, None)
        handler._is_home = MagicMock(return_value=True)
        self.assertEqual(True, handler._is_anyone_home())
        handler._is_home.assert_called_once_with("123")

    def test_should_update_presence_time_if_someone_home(self):
        configuration = Configuration()
        configuration.ip = ["123", "234"]
        handler = MotionDetectionHandler(configuration, None)
        handler._is_anyone_home = MagicMock(return_value=True)
        last_presence_time = datetime.now() - timedelta(days=1)
        handler.last_presence_time = last_presence_time
        handler.process(1)
        handler._is_anyone_home.assert_called_once_with()
        self.assertTrue(handler.last_presence_time > last_presence_time)

    def test_should_not_update_presence_time_if_too_soon(self):
        configuration = Configuration()
        configuration.ip = ["123", "234"]
        handler = MotionDetectionHandler(configuration, None)
        last_presence_time = datetime.now() - timedelta(minutes=5)
        handler._is_anyone_home = MagicMock(return_value=True)
        handler.last_presence_time = last_presence_time
        handler.process(1)
        self.assertEqual(handler.last_presence_time, last_presence_time)
        self.assertFalse(handler._is_anyone_home.called)

    def test_should_send_message(self):
        configuration = Configuration()
        configuration.ip = ["123", "234"]
        handler = MotionDetectionHandler(configuration, None)
        handler._is_anyone_home = MagicMock(return_value=False)
        handler._send_video = MagicMock()
        handler.telegram_service = MagicMock()
        handler.last_presence_time = datetime.now() - timedelta(days=1)
        handler.process(10)
        handler.telegram_service.send_to_all.assert_called_once_with({'message_text': 'Motion on channel 10'})
        handler._send_video.assert_called_once_with()
