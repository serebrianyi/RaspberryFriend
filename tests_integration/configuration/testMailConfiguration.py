import unittest
from RaspberryFriend.configuration.Configuration import Configuration
from RaspberryFriend.configuration.ConfigurationEnum import ConfigurationEnum


class MailConfigurationITCase(unittest.TestCase):

    def test_should_initialize_mail_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Mail)
        self.assertIsNotNone(configuration.server_name)
        self.assertIsNotNone(configuration.username)
        self.assertIsNotNone(configuration.password)
        self.assertIsNotNone(configuration.subject)
        self.assertIsNotNone(configuration.from_address)
        self.assertIsNotNone(configuration.recipients)
        self.assertIsNotNone(configuration.message)
