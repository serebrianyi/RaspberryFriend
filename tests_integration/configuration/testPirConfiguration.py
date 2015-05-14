import unittest
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class PirConfigurationITCase(unittest.TestCase):

    def test_should_initialize_gpio_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Pir)
        self.assertIsNotNone(configuration.pir_pin)



