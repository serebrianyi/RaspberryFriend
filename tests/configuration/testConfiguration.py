import unittest
from RaspberryFriend.configuration.Configuration import Configuration
from mock import MagicMock


class ConfigurationTestCase(unittest.TestCase):

    def test_should_initialize_properties(self):
        configuration = Configuration()
        configuration._get_file_content = MagicMock(return_value='{"name": "test_name", "password": "test_password"}')
        configuration.load("test")
        self.assertEqual("test_name", configuration.name)
        self.assertEqual("test_password", configuration.password)

    def test_should_initialize_map_properties(self):
        configuration = Configuration()
        configuration._get_file_content = MagicMock(return_value='{"arr": {"name": "test_name", "name2": "test_name2"}}')
        configuration.load("test")
        self.assertEqual("test_name", configuration.arr["name"])

