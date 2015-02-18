import unittest
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class QuoteConfigurationITCase(unittest.TestCase):

    def test_should_initialize_quote_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Quote)
        self.assertIsNotNone(configuration.quotes)



