import picamera
from RaspberryFriend.domain_services.mail_service.MailService import MailService
import os
from RaspberryFriend.util.DateUtil import DateUtil


class VideoHandler(object):

    def process(self, length):
        filename = self._get_filename()
        self._record(filename, length)
        self._send_mail_to_all(filename)
        return "An e-mail with video %s was sent" % filename

    def process_to_sender(self, sender, length):
        filename = self._get_filename()
        self._record(filename, length)
        self._send_mail_to_sender(sender, filename)
        return "An e-mail with video %s was sent" % filename

    def _record(self, filename, length):
        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.start_recording(filename)
            camera.wait_recording(length)
            camera.stop_recording()

    def _send_mail_to_all(self, filename):
        MailService().send_to_all(filename)

    def _send_mail_to_sender(self, sender, filename):
        MailService().send(sender, filename)

    def _get_filename(self):
        return os.path.join(os.path.dirname(__file__), "videos/%s.h264" % DateUtil.get_current_datetime_as_filename())