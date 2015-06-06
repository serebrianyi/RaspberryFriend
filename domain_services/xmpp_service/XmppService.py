from commands.CommandFactory import CommandFactory
from commands.UnauthorizedCommand import UnauthorizedCommand
from sleekxmpp import ClientXMPP
import os
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

    def check_recipient_params(self, params):
        first_param = params.strip().find(" ")
        if first_param > -1:
            pi_name = params[:first_param].lower()
            if pi_name == self.configuration.pi_name:
                return params[first_param:].strip()
            else:
                if self.configuration.is_master and pi_name not in self.configuration.slaves:
                    return params
        else:
            if self.configuration.is_master:
                return params

    # Message gets accepted if
    # (1) Type is chat or normal
    # (2) Sender is authorized
    # (3) Correct recipient
    def message(self, msg):
        LoggingService.info("----------------------------------")
        if msg["from"] in self.configuration.allowed_access:
            if msg['type'] in ('chat', 'normal'):
                body = self.check_recipient_params(msg['body'])
                if body is not None:
                    LoggingService.info("Authorized access with msg type " + msg['type'])
                    LoggingService.info("Processing command " + body)
                    command = CommandFactory.create_command(body)
                    try:
                        self.reply(msg, command.process(msg['from']))
                    except Exception as inst:
                        LoggingService.exception(inst)
                        return self.reply(msg, str(inst))
                else:
                    LoggingService.info("Different recipient")
        else:
            LoggingService.info("Unauthorized access")
            return self.reply(msg, UnauthorizedCommand(None).process(msg['from']))
        LoggingService.info("----------------------------------")

    def reply(self, source_msg, reply_text):
        source_msg.reply("(" + self.configuration.pi_name + ")" + os.linesep + reply_text).send()

    def send_to_all(self, msg):
        for recipient in self.configuration.allowed_access:
            self.send_message(recipient, msg, 'chat')