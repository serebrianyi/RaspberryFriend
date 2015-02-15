import unittest
from mock import MagicMock
from RaspberryFriend.commands.TramCommand import TramCommand
from RaspberryFriend.configuration.Configuration import Configuration
from RaspberryFriend.handlers.TramHandler import TramHandler


class TramCommandTestCase(unittest.TestCase):

    def test_should_call_tram_handler(self):
         configuration = Configuration()
         configuration.home_address = "src"
         configuration.work_address = {"sender": { "target": "dest", "waypoint": "point"}}
         handler = TramHandler()
         handler.process = MagicMock(return_value="from src to dest")
         command = TramCommand(None)
         command._get_tram_configuration = MagicMock(return_value=configuration)
         command._get_tram_handler = MagicMock(return_value=handler)
         self.assertEqual("from src to dest", command.process("sender"))

    def test_should_call_tram_handler_home(self):
         configuration = Configuration()
         configuration.home_address = "home"
         configuration.work_address = {"sender": { "target": "work", "waypoint": "point"}}
         handler = TramHandler()
         handler.process = MagicMock(return_value="")
         command = TramCommand("home")
         command._get_tram_configuration = MagicMock(return_value=configuration)
         command._get_tram_handler = MagicMock(return_value=handler)
         command.process("sender")
         handler.process.assert_called_once_with("work", "home", "point")

    def test_should_call_tram_handler_work(self):
         configuration = Configuration()
         configuration.home_address = "home"
         configuration.work_address = {"sender": { "target": "work", "waypoint": "point"}}
         handler = TramHandler()
         handler.process = MagicMock(return_value="")
         command = TramCommand("work")
         command._get_tram_configuration = MagicMock(return_value=configuration)
         command._get_tram_handler = MagicMock(return_value=handler)
         command.process("sender")
         handler.process.assert_called_once_with("home", "work", "point")

    def test_should_call_tram_handler_default(self):
         configuration = Configuration()
         configuration.home_address = "home"
         configuration.work_address = {"sender": { "target": "work", "waypoint": "point"}}
         handler = TramHandler()
         handler.process = MagicMock(return_value="")
         command = TramCommand(None)
         command._get_tram_configuration = MagicMock(return_value=configuration)
         command._get_tram_handler = MagicMock(return_value=handler)
         command.process("sender")
         handler.process.assert_called_once_with("home", "work", "point")

    def test_should_call_tram_handler_unknown_param(self):
         configuration = Configuration()
         configuration.home_address = "home"
         configuration.work_address = {"sender": { "target": "work", "waypoint": "point"}}
         handler = TramHandler()
         handler.process = MagicMock(return_value="")
         command = TramCommand("fake")
         self.assertEqual("Unknown tram params: fake", command.process("sender"))

