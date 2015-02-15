import unittest
from RaspberryFriend.configuration.Configuration import Configuration
from mock import MagicMock, call
from RaspberryFriend.domain_services.mail_service.MailService import MailService

class MailServiceTestCase(unittest.TestCase):

    def test_should_create_mail_from_configuration(self):
        configuration = Configuration()
        configuration.from_address = "from address"
        configuration.recipient = {"id": "mail"}
        configuration.subject = "subject"
        configuration.message = "text message"
        mail_service = MailService()
        mail = mail_service._create_message(configuration, "mail")
        self.assertEqual(configuration.from_address, mail['From'])
        self.assertEqual("mail", mail['To'])
        self.assertEqual(configuration.subject, mail['Subject'])
        self.assertTrue(configuration.message in str(mail.get_payload()[0].as_string()))

    def test_should_pass_message_to_server(self):
        configuration = Configuration()
        configuration.recipients = {"id1" : "mail1", "id2" : "mail2"}
        mail = {}
        mail_service = MailService()
        mail_service._get_configuration = MagicMock(return_value=configuration)
        mail_service._create_message = MagicMock(return_value=mail)
        mail_service._pass_message_to_server = MagicMock(return_value=None)
        mail_service.send_plain("id1")
        mail_service._pass_message_to_server.assert_called_once_with(mail, configuration, "mail1")

    def test_should_attach_file_to_message(self):
        configuration = Configuration()
        configuration.recipients = {"id1" : "mail1", "id2" : "mail2"}
        mail = {}
        mail_service = MailService()
        mail_service._get_configuration = MagicMock(return_value=configuration)
        mail_service._create_message = MagicMock(return_value=mail)
        mail_service._pass_message_to_server = MagicMock(return_value=None)
        mail_service._attach_file_to_message = MagicMock(return_value=None)
        mail_service.send_to_all("fake_file")
        self.assertEqual(mail_service._pass_message_to_server.mock_calls, [call(mail, configuration, "mail2"), call(mail, configuration, "mail1")])
        self.assertEqual(mail_service._attach_file_to_message.mock_calls, [call(mail, "fake_file"), call(mail, "fake_file")])

