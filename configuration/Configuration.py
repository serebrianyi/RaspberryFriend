import os
import json


class Configuration(object):

    def load(self, configuration_enum):
        self.__dict__ = json.loads(self._get_file_content(configuration_enum))

    def _get_file_content(self, configuration_enum):
        file = open(os.path.join(os.path.dirname(__file__), "files/%s.json" % configuration_enum), 'r')
        return file.read()
