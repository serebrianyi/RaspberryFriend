import unittest
from commands.CommandFactory import CommandFactory
from commands.UnknownCommand import UnknownCommand
from tests.commands.CommandMock import CommandMock


class CommandFactoryTestCase(unittest.TestCase):

    def test_should_create_new_command(self):
        factory = CommandFactory
        factory.commandMapping = {"status": CommandMock, "status2": None}
        command = CommandFactory.create_command("status")
        self.assertIsNotNone(command)
        self.assertEqual(None, command.params)

    def test_should_create_new_command_with_blanks(self):
        factory = CommandFactory
        factory.commandMapping = {"tram": CommandMock, "status2": None}
        command = CommandFactory.create_command(" Tram ")
        self.assertIsNotNone(command)
        self.assertEqual(None, command.params)

    def test_should_create_new_command_case_insensitive(self):
        factory = CommandFactory
        factory.commandMapping = {"status": CommandMock, "status2": None}
        command = CommandFactory.create_command("Status")
        self.assertIsNotNone(command)
        self.assertEqual(None, command.params)

    def test_should_create_new_command_with_passed_arguments(self):
        factory = CommandFactory
        factory.commandMapping = {"status": CommandMock}
        command = CommandFactory.create_command("status param1 param2")
        self.assertIsNotNone(command)
        self.assertEqual("param1 param2", command.params)

    def test_should_create_new_command_with_passed_arguments(self):
        factory = CommandFactory
        factory.commandMapping = {"status": CommandMock}
        command = CommandFactory.create_command("status2")
        self.assertIsNotNone(command)
        self.assertIsInstance(command, UnknownCommand)
        self.assertEqual({"message_text": "Unknown command"}, command.process("reer"))


