import unittest
from RaspberryFriend.configuration.Configuration import Configuration
from RaspberryFriend.configuration.ConfigurationEnum import ConfigurationEnum


class GpioConfigurationITCase(unittest.TestCase):

    def test_should_initialize_gpio_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Gpio)
        self.assertIsNotNone(configuration.pir_pin)



