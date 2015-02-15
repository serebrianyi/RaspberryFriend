from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum
from domain_services.xmpp_service.XmppService import XmppService
from mock import MagicMock
import os

class TestUtil(object):

    @staticmethod
    def get_xmpp_authorized_user():
        configuration_xmpp = Configuration()
        configuration_xmpp.load(ConfigurationEnum.Xmpp)
        return configuration_xmpp.allowed_access[0]

    @staticmethod
    def get_xmpp_message(body):
        return {"from": TestUtil.get_xmpp_authorized_user(), "type" : "chat", "body" : body}

    @staticmethod
    def get_xmpp_response(body):
        return {'body': body, 'type': 'chat', 'from': TestUtil.get_xmpp_authorized_user()}

    @staticmethod
    def get_xmpp_service():
        configuration_xmpp = Configuration()
        configuration_xmpp.load(ConfigurationEnum.Xmpp)
        xmpp_service = XmppService(configuration_xmpp)
        xmpp_service.reply = MagicMock(return_value=None)
        return xmpp_service

    @staticmethod
    def get_current_directory(file):
        return os.path.dirname(file).replace("tests_integration%s" % os.path.sep, "")