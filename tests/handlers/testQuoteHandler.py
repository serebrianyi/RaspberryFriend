import unittest
from handlers.QuoteHandler import QuoteHandler
from mock import MagicMock, call
import json
from configuration.Configuration import Configuration
import os


class QuoteHandlerTestCase(unittest.TestCase):

    def test_should_process(self):
        jsonString = """{
                      "list": {
                        "meta": {
                          "type": "resource-list",
                          "start": 0,
                          "count": 1
                        },
                        "resources": [
                          {
                            "resource": {
                              "classname": "Quote",
                              "fields": {
                                "name": "TEST",
                                "price": "304.799988",
                                "symbol": "test",
                                "ts": "1423844736",
                                "type": "equity",
                                "utctime": "2015-02-13T16:25:36+0000",
                                "volume": "627362"
                              }
                            }
                          }
                        ]
                      }
                    }"""
        handler = QuoteHandler()
        handler._get_response = MagicMock(return_value=json.loads(jsonString))
        configuration  = Configuration()
        configuration.quotes = ["testquote1", "testquote2"]
        handler._get_configuration = MagicMock(return_value=configuration)

        self.assertEqual({"message_text": "testquote1: 304.799988{0}testquote2: 304.799988{0}".format(os.linesep)}, handler.process())
        self.assertEqual(handler._get_response.mock_calls, [call('testquote1'), call('testquote2')])




