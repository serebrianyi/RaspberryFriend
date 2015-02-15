from commands.AbstractCommand import AbstractCommand
from handlers.VideoHandler import VideoHandler


class VideoCommand(AbstractCommand):

    def process(self, sender):
        if self.params is None:
            length = 5
        else:
            length = int(self.params.strip())
        return self._get_video_handler().process_to_sender(sender, length)

    def _get_video_handler(self):
        return VideoHandler()


