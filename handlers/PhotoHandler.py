from domain_services.camera_service.CameraService import CameraService
import os
from domain_services.mail_service.MailService import MailService
from util.DateUtil import DateUtil


class PhotoHandler(object):

    def process(self):
        filename = self._get_filename()
        self._record(filename)
        self._get_mail_service().send_to_all(filename)
        return "An e-mail with photo %s was sent" % filename

    def process_to_sender(self, sender):
        filename = self._get_filename()
        self._record(filename)
        self._get_mail_service().send(sender, filename)
        return "An e-mail with photo %s was sent" % filename

    def _record(self, filename):
        CameraService.record_photo(filename)

    def _get_mail_service(self):
        return MailService()

    def _get_filename(self):
        return os.path.join(os.path.dirname(__file__), "photos/%s.jpg" % DateUtil.get_current_datetime_as_filename())