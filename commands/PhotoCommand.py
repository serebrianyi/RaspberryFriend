from commands.AbstractCommand import AbstractCommand
from handlers.PhotoHandler import PhotoHandler


class PhotoCommand(AbstractCommand):

    def process(self, sender):
        return PhotoHandler().process_to_sender(sender)


