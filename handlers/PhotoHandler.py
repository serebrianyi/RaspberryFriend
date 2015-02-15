import picamera
import os
from RaspberryFriend.domain_services.mail_service.MailService import MailService
from RaspberryFriend.util.DateUtil import DateUtil


class PhotoHandler(object):

    def process(self):
        filename = self._get_filename()
        self._record(filename)
        self._send_mail_to_all(filename)
        return "An e-mail with photo %s was sent" % filename

    def process_to_sender(self, sender):
        filename = self._get_filename()
        self._record(filename)
        self._send_mail_to_sender(sender, filename)
        return "An e-mail with photo %s was sent" % filename

    def _record(self, filename):
        with picamera.PiCamera() as camera:
            camera.resolution = (2592, 1944)
            camera.start_preview()
            camera.capture(filename)
            camera.stop_preview()

    def _send_mail_to_all(self, filename):
        MailService().send_to_all(filename)

    def _send_mail_to_sender(self, sender, filename):
        MailService().send(sender, filename)

    def _get_filename(self):
        return os.path.join(os.path.dirname(__file__), "photos/%s.jpg" % DateUtil.get_current_datetime_as_filename())