import unittest
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class TelegramConfigurationITCase(unittest.TestCase):

    def test_should_initialize_telegram_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Telegram)
        self.assertIsNotNone(configuration.token)
        self.assertIsNotNone(configuration.url)
        self.assertIsNotNone(configuration.interval)
        self.assertIsNotNone(configuration.allowed_access)
        self.assertIsNotNone(configuration.pi_name)
        self.assertIsNotNone(configuration.slaves)
        self.assertIsNotNone(configuration.is_master)




