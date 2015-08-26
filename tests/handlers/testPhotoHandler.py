import unittest
from handlers.PhotoHandler import PhotoHandler
from mock import MagicMock, call


class PhotoHandlerTestCase(unittest.TestCase):

    def test_should_process(self):
        handler = PhotoHandler()
        handler._record = MagicMock()
        handler._get_filename = MagicMock(return_value="test_name")

        self.assertEqual({"photo_filename": "test_name"}, handler.process())

