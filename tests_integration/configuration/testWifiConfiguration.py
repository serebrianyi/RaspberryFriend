import unittest
from RaspberryFriend.configuration.Configuration import Configuration
from RaspberryFriend.configuration.ConfigurationEnum import ConfigurationEnum


class WifiConfigurationITCase(unittest.TestCase):

    def test_should_initialize_wifi_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Wifi)
        self.assertIsNotNone(configuration.ip)



