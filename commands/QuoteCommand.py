from commands.AbstractCommand import AbstractCommand
from handlers.QuoteHandler import QuoteHandler

# Command to get the stock quotes
class QuoteCommand(AbstractCommand):

    def process(self, sender):
        return QuoteHandler().process()


