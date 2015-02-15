from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum
from domain_services.logging_service.LoggingService import LoggingService
from domain_services.xmpp_service.XmppService import XmppService
from domain_services.motion_detection_service.MotionDetectionService import MotionDetectionService
from handlers.MotionDetectionHandler import MotionDetectionHandler

if __name__ == '__main__':
    configuration_xmpp = Configuration()
    configuration_xmpp.load(ConfigurationEnum.Xmpp)
    LoggingService.info("Start xmpp service")
    xmpp_service = XmppService(configuration_xmpp)
    LoggingService.info("Connecting..")
    xmpp_service.connect()
    LoggingService.info("Connected")
    configuration_wifi = Configuration()
    configuration_wifi.load(ConfigurationEnum.Wifi)
    motion_detection_handler = MotionDetectionHandler(configuration_wifi, xmpp_service)
    motion_detection_service = MotionDetectionService()
    motion_detection_service.startObservation(motion_detection_handler.process)
    xmpp_service.process(block=True)