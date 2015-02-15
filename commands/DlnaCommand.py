from RaspberryFriend.commands.AbstractCommand import AbstractCommand
from RaspberryFriend.handlers.DlnaHandler import DlnaHandler


class DlnaCommand(AbstractCommand):

    def process(self, sender):
        return DlnaHandler().process()


