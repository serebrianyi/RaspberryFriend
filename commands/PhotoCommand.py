from commands.AbstractCommand import AbstractCommand
from handlers.PhotoHandler import PhotoHandler

# Command to make a photo and send it per mail
class PhotoCommand(AbstractCommand):

    def process(self, sender):
        return PhotoHandler().process_to_sender(sender)


