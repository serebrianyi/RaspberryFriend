from RaspberryFriend.commands.AbstractCommand import AbstractCommand
from RaspberryFriend.handlers.PhotoHandler import PhotoHandler


class PhotoCommand(AbstractCommand):

    def process(self, sender):
        return PhotoHandler().process_to_sender(sender)


