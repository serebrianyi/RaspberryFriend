import picamera


class CameraService(object):

    @classmethod
    def record_video(cls, filename, length):
        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.start_recording(filename)
            camera.wait_recording(length)
            camera.stop_recording()

    @classmethod
    def record_photo(cls, filename):
        with picamera.PiCamera() as camera:
            camera.resolution = (2592, 1944)
            camera.start_preview()
            camera.capture(filename)
            camera.stop_preview()