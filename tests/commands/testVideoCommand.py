import unittest
from mock import MagicMock
from RaspberryFriend.commands.VideoCommand import VideoCommand
from RaspberryFriend.handlers.VideoHandler import VideoHandler


class VideoCommandTestCase(unittest.TestCase):

    def test_should_call_video_handler(self):
         handler = VideoHandler()
         handler.process_to_sender = MagicMock(return_value="return test value")
         command = VideoCommand(None)
         command._get_video_handler = MagicMock(return_value=handler)
         self.assertEqual("return test value", command.process("sender"))
         handler.process_to_sender.assert_called_once_with("sender", 5)

    def test_should_call_video_handler_with_specific_time_value(self):
         handler = VideoHandler()
         handler.process_to_sender = MagicMock(return_value="return test value")
         command = VideoCommand("10")
         command._get_video_handler = MagicMock(return_value=handler)
         self.assertEqual("return test value", command.process("sender"))
         handler.process_to_sender.assert_called_once_with("sender", 10)