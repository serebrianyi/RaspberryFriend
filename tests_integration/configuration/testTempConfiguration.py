import unittest
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class TempConfigurationITCase(unittest.TestCase):

    def test_should_initialize_temp_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Temp)
        self.assertIsNotNone(configuration.pin)
        self.assertIsNotNone(configuration.model)



