import subprocess
from datetime import datetime
from domain_services.logging_service.LoggingService import LoggingService
from handlers.VideoHandler import VideoHandler


class MotionDetectionHandler(object):

    TIME_TO_WAIT = 60*20

    def __init__(self, configuration, telegram_service):
        self.telegram_service = telegram_service
        self.last_presence_time = datetime.now()
        self.configuration = configuration

    def process(self, channel):
        # we check presence only every 20 min
        #if (datetime.now() - self.last_presence_time).total_seconds() > self.TIME_TO_WAIT:
        if (datetime.now() - self.last_presence_time).total_seconds() > 1:
            if not self._is_anyone_home():
                LoggingService().info("Motion detected.")
                self.telegram_service.send_to_all({"message_text": "Motion on channel %s" % channel})
                self._send_video()
            else:
                LoggingService().info("Someone is home. Update last presence time.")
                self.last_presence_time = datetime.now()

    def _send_video(self):
        self.telegram_service.send_to_all(VideoHandler().process(5))

    # check 1 time if a specific ip is reachable
    def _is_home(self, ip):
        ret = subprocess.call(['ping', '-c', '1', '-W', '1', ip], stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
        return True if ret == 0 else False

    # check if any of the registered ips is reachable
    # we iterate through them 3 times to decrease the chance of false positive
    # this is also better then just to ping the same ip 3 times in a row
    def _is_anyone_home(self):
        for n in range(0, 2):
            for ip in self.configuration.ip:
                if self._is_home(ip):
                    return True
        return False
