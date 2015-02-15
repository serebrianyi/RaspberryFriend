import unittest
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class TramConfigurationITCase(unittest.TestCase):

    def test_should_initialize_tram_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Tram)
        self.assertIsNotNone(configuration.home_address)
        self.assertIsNotNone(configuration.work_address)



