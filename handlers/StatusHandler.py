from util.DateUtil import DateUtil


class StatusHandler(object):

    def process(self):
        return {"message_text" : "RaspberryPi is on. Current time: " + DateUtil.get_current_datetime_as_string()}