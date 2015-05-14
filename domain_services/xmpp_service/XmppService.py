from commands.CommandFactory import CommandFactory
from commands.UnauthorizedCommand import UnauthorizedCommand
from sleekxmpp import ClientXMPP
from domain_services.logging_service.LoggingService import LoggingService


class XmppService(ClientXMPP):

    def __init__(self, configuration):
        self.configuration = configuration
        ClientXMPP.__init__(self, configuration.name, configuration.password)
        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

    # Message gets accepted if
    # (1) Type is chat or normal
    # (2) Sender is authorized
    def message(self, msg):
        LoggingService.info("----------------------------------")
        if msg["from"] in self.configuration.allowed_access:
            LoggingService.info("Authorized access with msg type " + msg['type'])
            if msg['type'] in ('chat', 'normal'):
                command = CommandFactory.create_command(msg['body'])
                try:
                    self.reply(msg, command.process(msg['from']))
                except Exception as inst:
                    LoggingService.exception(inst)
                    return self.reply(msg, str(inst))
        else:
            LoggingService.info("Unauthorized access")
            return self.reply(msg, UnauthorizedCommand(None).process(msg['from']))
        LoggingService.info("----------------------------------")

    def reply(self, source_msg, reply_text):
        source_msg.reply(reply_text).send()

    def send_to_all(self, msg):
        for recipient in self.configuration.allowed_access:
            self.send_message(recipient, msg, 'chat')