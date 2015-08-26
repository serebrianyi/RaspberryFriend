import unittest
from handlers.VideoHandler import VideoHandler
from mock import MagicMock, call



class VideoHandlerTestCase(unittest.TestCase):

   def test_should_process(self):
        handler = VideoHandler()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual({"video_filename": "test_name"}, handler.process(5))

