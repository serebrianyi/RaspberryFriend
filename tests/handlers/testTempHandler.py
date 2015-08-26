import unittest
from handlers.TempHandler import TempHandler
from mock import MagicMock
import sys
sys.modules['Adafruit_DHT'] = MagicMock()


class TempHandlerTestCase(unittest.TestCase):

    def test_should_process(self):
        handler = TempHandler()
        handler._get_temp = MagicMock(return_value=[1, 2])
        self.assertEqual({"message_text": "Temp=2.0*C  Humidity=1.0%"}, handler.process(5, 6))
        handler._get_temp.assert_called_once_with(5, 6)

