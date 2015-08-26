from domain_services.camera_service.CameraService import CameraService
import os

from util.DateUtil import DateUtil

class PhotoHandler(object):

    def process(self):
        filename = self._get_filename()
        self._record(filename)
        return {"photo_filename": filename}

    def _record(self, filename):
        CameraService.record_photo(filename)

    def _get_filename(self):
        return os.path.join(os.path.dirname(__file__), "photos/%s.jpg" % DateUtil.get_current_datetime_as_filename())