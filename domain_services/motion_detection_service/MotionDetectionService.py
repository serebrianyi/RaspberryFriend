import RPi.GPIO as GPIO
from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum


class MotionDetectionService(object):

    def startObservation(self, callback):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Pir)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(configuration.pir_pin,GPIO.IN)
        GPIO.add_event_detect(configuration.pir_pin, GPIO.RISING, callback, bouncetime=300)