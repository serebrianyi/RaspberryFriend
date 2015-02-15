import os
import smtplib
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


class MailService(object):

    def send_plain(self, recipient):
        configuration = self._get_configuration()
        recipientMail = configuration.recipients[recipient]
        mail = self._create_message(configuration, recipientMail)
        self._pass_message_to_server(mail, configuration, recipientMail)

    def send_to_all(self, filename):
        configuration = self._get_configuration()
        for key in configuration.recipients:
            self.send(key, filename)

    def send(self, recipient, filename):
        configuration = self._get_configuration()
        recipientMail = configuration.recipients[recipient]
        mail = self._create_message(configuration, recipientMail)
        self._attach_file_to_message(mail, filename)
        self._pass_message_to_server(mail, configuration, recipientMail)

    def _create_message(self, configuration, recipient):
        mail = MIMEMultipart()
        mail['From'] = configuration.from_address
        mail['To'] = recipient
        mail['Subject'] = configuration.subject
        mail.attach(MIMEText(configuration.message))
        return mail

    def _get_configuration(self):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Mail)
        return configuration

    def _attach_file_to_message(self, mail, filename):
        part = MIMEBase('application', "octet-stream")
        with open(filename, "rb") as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filename))
        mail.attach(part)

    def _pass_message_to_server(self, mail, configuration, recipient):
        smtp = smtplib.SMTP(configuration.server_name)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(configuration.username, configuration.password)
        smtp.sendmail(configuration.from_address, recipient, mail.as_string())
        smtp.quit()

