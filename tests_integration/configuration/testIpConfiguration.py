import unittest
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class IpConfigurationITCase(unittest.TestCase):

    def test_should_initialize_wifi_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Ip)
        self.assertIsNotNone(configuration.ip)



