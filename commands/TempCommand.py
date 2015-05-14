from commands.AbstractCommand import AbstractCommand
from handlers.TempHandler import TempHandler
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


# Command to get the current temperature
class TempCommand(AbstractCommand):

    def process(self, sender):
        configuration = self._get_temp_configuration()
        return TempHandler().process(configuration.model, configuration.pin)

    def _get_temp_configuration(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Temp)
        return configuration
