from RaspberryFriend.commands.StatusCommand import StatusCommand
from RaspberryFriend.commands.UnknownCommand import UnknownCommand
from RaspberryFriend.commands.TramCommand import TramCommand
from RaspberryFriend.commands.DlnaCommand import DlnaCommand
from RaspberryFriend.commands.PhotoCommand import PhotoCommand
from RaspberryFriend.commands.VideoCommand import VideoCommand


class CommandFactory(object):

    commandMapping = {"status": StatusCommand,
                      "tram": TramCommand,
                      "dlna": DlnaCommand,
                      "photo": PhotoCommand,
                      "video": VideoCommand
    }

    @classmethod
    def create_command(cls, params):
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




