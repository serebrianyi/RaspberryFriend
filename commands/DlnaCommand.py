from commands.AbstractCommand import AbstractCommand
from handlers.DlnaHandler import DlnaHandler


# Command to restart the dlna media server
class DlnaCommand(AbstractCommand):

    def process(self, sender):
        return DlnaHandler().process()


