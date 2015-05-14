import unittest
from configuration.Configuration import Configuration
from mock import MagicMock
import sys
sys.modules['domain_services.logging_service.LoggingService'] = MagicMock()
from domain_services.xmpp_service.XmppService import XmppService


class XmppServiceITCase(unittest.TestCase):

    def test_should_not_allow_unauthorized(self):
        configuration = Configuration()
        configuration.name = "name"
        configuration.password = "password"
        configuration.allowed_access = ["user1", "user2"]
        xmpp_service = XmppService(configuration)
        msg = dict()
        msg["from"] = "no_user"
        xmpp_service.reply = MagicMock(return_value=None)
        xmpp_service.message(msg)
        xmpp_service.reply.assert_called_once_with({'from': 'no_user'}, "Unauthorized access from no_user")

    def test_should_allow_only_chat_and_normal_type(self):
        configuration = Configuration()
        configuration.name = "name"
        configuration.password = "password"
        configuration.allowed_access = ["user1", "user2"]
        xmpp_service = XmppService(configuration)
        msg = dict()
        msg["from"] = "user1"
        msg["body"] = "status"
        msg["type"] = "fake"
        xmpp_service._info = MagicMock()
        xmpp_service.reply = MagicMock(return_value=None)
        xmpp_service.message(msg)
        self.assertEqual(0, xmpp_service.reply.call_count)

    def test_should_process_command(self):
        configuration = Configuration()
        configuration.name = "name"
        configuration.password = "password"
        configuration.allowed_access = ["user1", "user2"]
        xmpp_service = XmppService(configuration)
        msg = dict()
        msg["from"] = "user1"
        msg["body"] = "status"
        msg["type"] = "chat"
        xmpp_service.reply = MagicMock(return_value=None)
        xmpp_service.message(msg)
        xmpp_service.reply.assert_called_once_with({'body': 'status', 'type': 'chat', 'from': 'user1'}, None)
