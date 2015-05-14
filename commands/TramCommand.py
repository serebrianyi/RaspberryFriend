from commands.AbstractCommand import AbstractCommand
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum
from handlers.TramHandler import TramHandler


# Command to get the tram connection
class TramCommand(AbstractCommand):

    def process(self, sender):
        configuration = self._get_tram_configuration()
        # default is "work"
        # other option is "home"
        if self.params is None or self.params.lower() == "work":
            return self._get_tram_handler().process(configuration.home_address,
                                                    configuration.work_address[sender]["target"],
                                                    configuration.work_address[sender]["waypoint"]
                                                    )
        elif self.params.lower() == "home":
            return self._get_tram_handler().process(configuration.work_address[sender]["target"],
                                                    configuration.home_address,
                                                    configuration.work_address[sender]["waypoint"])
        else:
            return "Unknown tram params: " + self.params

    def _get_tram_handler(self):
        return TramHandler()

    def _get_tram_configuration(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Tram)
        return configuration


