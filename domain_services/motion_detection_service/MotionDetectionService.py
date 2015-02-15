import RPi.GPIO as GPIO
from RaspberryFriend.configuration.Configuration import Configuration
from RaspberryFriend.configuration.ConfigurationEnum import ConfigurationEnum


class MotionDetectionService(object):

    def startObservation(self, callback):
        configuration = Configuration()
        configuration.load(ConfigurationEnum.Gpio)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(configuration.pir_pin,GPIO.IN)
        GPIO.add_event_detect(configuration.pir_pin, GPIO.RISING, callback, bouncetime=300)