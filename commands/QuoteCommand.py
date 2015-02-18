from commands.AbstractCommand import AbstractCommand
from handlers.QuoteHandler import QuoteHandler


class QuoteCommand(AbstractCommand):

    def process(self, sender):
        return QuoteHandler().process()


