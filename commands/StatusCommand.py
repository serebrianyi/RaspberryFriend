from commands.AbstractCommand import AbstractCommand
from handlers.StatusHandler import StatusHandler

# Command to get the current raspberry pi status
class StatusCommand(AbstractCommand):

    def process(self, sender):
        return StatusHandler().process()


