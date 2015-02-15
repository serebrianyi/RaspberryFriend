import unittest
from RaspberryFriend.configuration.Configuration import Configuration
from RaspberryFriend.configuration.ConfigurationEnum import ConfigurationEnum


class XmppConfigurationITCase(unittest.TestCase):

    def test_should_initialize_xmpp_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Xmpp)
        self.assertIsNotNone(configuration.name)
        self.assertIsNotNone(configuration.password)
        self.assertIsNotNone(configuration.allowed_access)



