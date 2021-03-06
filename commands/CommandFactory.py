from commands.StatusCommand import StatusCommand
from commands.UnknownCommand import UnknownCommand
from commands.TramCommand import TramCommand
from commands.DlnaCommand import DlnaCommand
from commands.PhotoCommand import PhotoCommand
from commands.VideoCommand import VideoCommand
from commands.QuoteCommand import QuoteCommand
from commands.TempCommand import TempCommand


class CommandFactory(object):

    commandMapping = {"status": StatusCommand,
                      "tram": TramCommand,
                      "dlna": DlnaCommand,
                      "photo": PhotoCommand,
                      "video": VideoCommand,
                      "quotes": QuoteCommand,
                      "temp": TempCommand
    }

    @classmethod
    def create_command(cls, params):
        # first word in the message is the command mapped
        # everything else are parameters
        first_param = params.strip().find(" ")
        if first_param > -1:
            command_name = params[:first_param].lower()
            parameters = params[first_param:].strip()
        else:
            command_name = params.lower().strip()
            parameters = None

        if command_name in cls.commandMapping:
            return cls.commandMapping[command_name](parameters)
        else:
            return UnknownCommand(None)




