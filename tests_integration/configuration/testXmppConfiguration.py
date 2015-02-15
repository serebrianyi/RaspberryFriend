import unittest
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class XmppConfigurationITCase(unittest.TestCase):

    def test_should_initialize_xmpp_properties(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Xmpp)
        self.assertIsNotNone(configuration.name)
        self.assertIsNotNone(configuration.password)
        self.assertIsNotNone(configuration.allowed_access)



