from datetime import datetime
import time


class DateUtil(object):

    @staticmethod
    def get_current_datetime_as_string():
        return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def get_current_datetime_as_filename():
        return datetime.now().strftime("%d_%m_%y_%H_%M")

    @staticmethod
    def get_current_time():
        return time.time()