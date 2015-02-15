import abc


class AbstractCommand(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, params):
        self.params = params

    @abc.abstractmethod
    def process(self, sender):
        return
