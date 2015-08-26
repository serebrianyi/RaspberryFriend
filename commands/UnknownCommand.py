from commands.AbstractCommand import AbstractCommand


class UnknownCommand(AbstractCommand):

    def process(self, sender):
        return {"message_text": "Unknown command"}


