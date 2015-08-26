from commands.AbstractCommand import AbstractCommand
from handlers.VideoHandler import VideoHandler


# Command to make a video and send it per mail
class VideoCommand(AbstractCommand):

    def process(self, sender):
        # video length as parameter (in seconds)
        # default is 5
        if self.params is None:
            length = 5
        else:
            length = int(self.params.strip())
        return self._get_video_handler().process(length)

    def _get_video_handler(self):
        return VideoHandler()


