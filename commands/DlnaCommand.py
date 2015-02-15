from commands.AbstractCommand import AbstractCommand
from handlers.DlnaHandler import DlnaHandler


class DlnaCommand(AbstractCommand):

    def process(self, sender):
        return DlnaHandler().process()


