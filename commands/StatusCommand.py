from commands.AbstractCommand import AbstractCommand
from handlers.StatusHandler import StatusHandler


class StatusCommand(AbstractCommand):

    def process(self, sender):
        return StatusHandler().process()


