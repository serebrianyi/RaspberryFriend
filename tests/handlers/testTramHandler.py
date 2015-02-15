import unittest
from handlers.TramHandler import TramHandler
from mock import MagicMock, call
import json
import time

class TramHandlerTestCase(unittest.TestCase):

    def test_should_process(self):
        jsonString = """{
                   "routes" : [
                      {
                         "legs" : [
                            {
                               "arrival_time" : {
                                  "text" : "15:19",
                                  "value" : 1423405140
                               },
                               "departure_time" : {
                                  "text" : "14:41",
                                  "value" : 1423402887
                               },
                               "steps" : [
                                  {
                                     "transit_details" : {
                                        "arrival_time" : {
                                           "text" : "15:13",
                                           "value" : 1423404780
                                        },
                                        "departure_time" : {
                                           "text" : "14:46",
                                           "value" : 1423403160
                                        },
                                        "line" : {
                                           "short_name" : "11"
                                        }
                                     }
                                  }
                               ]
                            }
                         ]
                      }
                   ]
                }"""
        handler = TramHandler()
        handler._get_response = MagicMock(return_value=json.loads(jsonString))
        handler._get_current_time = MagicMock(return_value=time.time())

        self.assertEqual("Leave at 14:41 (11,11 - wait for 0 min)", handler.process("src", "dest", "waypoint"))
        self.assertEqual(handler._get_response.mock_calls, [call('src', 'waypoint', str(int(time.time()))), call('waypoint', 'dest', '1423402887')])




