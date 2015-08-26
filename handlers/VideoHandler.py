from domain_services.camera_service.CameraService import CameraService
import os
from util.DateUtil import DateUtil


class VideoHandler(object):

    def process(self, length):
        filename = self._get_filename()
        self._record(filename, length)
        return {"video_filename": filename}

    def _record(self, filename, length):
        CameraService.record_video(filename, length)

    def _get_filename(self):
        return os.path.join(os.path.dirname(__file__), "videos/%s.h264" % DateUtil.get_current_datetime_as_filename())