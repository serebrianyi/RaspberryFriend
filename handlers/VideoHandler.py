from domain_services.mail_service.MailService import MailService
from domain_services.camera_service.CameraService import CameraService
import os
from util.DateUtil import DateUtil


class VideoHandler(object):

    def process(self, length):
        filename = self._get_filename()
        self._record(filename, length)
        self._get_mail_service().send_to_all(filename);
        return "An e-mail with video %s was sent" % filename

    def process_to_sender(self, sender, length):
        filename = self._get_filename()
        self._record(filename, length)
        self._get_mail_service().send(sender, filename);
        return "An e-mail with video %s was sent" % filename

    def _record(self, filename, length):
        CameraService.record_video(filename, length)

    def _get_mail_service(self):
        return MailService()

    def _get_filename(self):
        return os.path.join(os.path.dirname(__file__), "videos/%s.h264" % DateUtil.get_current_datetime_as_filename())