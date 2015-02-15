import subprocess
from datetime import datetime
from RaspberryFriend.domain_services.logging_service.LoggingService import LoggingService
from RaspberryFriend.handlers.VideoHandler import VideoHandler


class MotionDetectionHandler(object):

    def __init__(self, configuration, xmpp_service):
        self.xmpp_service = xmpp_service
        self.last_presence_time = datetime.now()
        self.configuration = configuration

    def process(self, channel):
        if (datetime.now() - self.last_presence_time).total_seconds() > 60*20:
            if not self._is_anyone_home():
                LoggingService().info("Motion detected.")
                self.xmpp_service.send_to_all("Motion on channel %s" % str(channel))
                self._send_video()
            else:
                LoggingService().info("Someone is home. Update last presence time.")
                self.last_presence_time = datetime.now()

    def _send_video(self):
        VideoHandler().process(5)

    def _is_home(self, ip):
        ret = subprocess.call(['ping', '-c', '1', '-W', '1', ip], stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
        return True if ret == 0 else False

    def _is_anyone_home(self):
        for n in range(0, 2):
            for ip in self.configuration.ip:
                if self._is_home(ip):
                    return True
        return False
