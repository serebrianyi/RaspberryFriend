from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum
import os
import requests

class QuoteHandler(object):

    def process(self):
        configuration = self._get_configuration()
        response = ""
        for quote in configuration.quotes:
            response += quote + ": " + self._get_response(quote)["list"]["resources"][0]["resource"]["fields"]["price"] \
                        + os.linesep
        return response

    def _get_response(self, quote):
        url = "http://finance.yahoo.com/webservice/v1/symbols/%s/quote?format=json" % quote
        r = requests.get(url)
        return r.json()

    def _get_configuration(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Quote)
        return configuration