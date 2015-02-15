from RaspberryFriend.commands.AbstractCommand import AbstractCommand


class UnauthorizedCommand(AbstractCommand):

    def process(self, sender):
        return "Unauthorized access from " + str(sender)


