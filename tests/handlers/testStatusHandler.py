import unittest
from handlers.StatusHandler import StatusHandler
from mock import patch
from util.DateUtil import DateUtil

class StatusHandlerTestCase(unittest.TestCase):

    def test_should_process(self):
        with patch.object(DateUtil, 'get_current_datetime_as_string', return_value="01.01.2015 12:13:14") as get_current_datetime_as_string:
            handler = StatusHandler()
            self.assertEqual("RaspberryPi is on. Current time: 01.01.2015 12:13:14", handler.process())
        get_current_datetime_as_string.assert_called_with()


