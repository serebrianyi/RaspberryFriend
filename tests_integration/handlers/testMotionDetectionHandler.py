import unittest
from datetime import datetime, timedelta

from tests_integration.util.TestUtil import TestUtil
from configuration.Configuration import Configuration
from mock import MagicMock
from handlers.MotionDetectionHandler import MotionDetectionHandler


class MotionDetectionHandlerITCase(unittest.TestCase):

    def test_should_process_when_nobody_home(self):
        configuration = Configuration()
        configuration.ip = ["192.168.0.0"]
        xmpp_service = TestUtil.get_xmpp_service()
        xmpp_service.send_to_all = MagicMock()
        handler = MotionDetectionHandler(configuration, xmpp_service)
        handler._send_video = MagicMock()
        handler.last_presence_time = datetime.now() - timedelta(days=1)
        handler.process(1)
        handler._send_video.assert_called_once_with()
        xmpp_service.send_to_all.assert_called_once_with("Motion on channel 1")

    def test_should_process_when_someone_home(self):
        configuration = Configuration()
        configuration.ip = ["173.194.116.88"]
        xmpp_service = TestUtil.get_xmpp_service()
        xmpp_service.send_to_all = MagicMock()
        handler = MotionDetectionHandler(configuration, xmpp_service)
        handler._send_video = MagicMock()
        last_presence_time = datetime.now() - timedelta(days=1)
        handler.last_presence_time = last_presence_time
        handler.process(1)
        self.assertTrue(handler.last_presence_time > last_presence_time)
        self.assertFalse(handler._send_video.called)

