from configuration.Configuration import Configuration
from configuration.ConfigurationEnum import ConfigurationEnum
from domain_services.logging_service.LoggingService import LoggingService
from domain_services.telegram_service.TelegramService import TelegramService
from domain_services.motion_detection_service.MotionDetectionService import MotionDetectionService
from handlers.MotionDetectionHandler import MotionDetectionHandler
import pexpect

if __name__ == '__main__':

    configuration_telegram = Configuration()
    configuration_telegram.load(ConfigurationEnum.Telegram)
    LoggingService.info("Start telegram service")
    telegram_service = TelegramService(configuration_telegram)
    configuration_wifi = Configuration()
    configuration_wifi.load(ConfigurationEnum.Ip)
    motion_detection_handler = MotionDetectionHandler(configuration_wifi, telegram_service)
    motion_detection_service = MotionDetectionService()
    motion_detection_service.startObservation(motion_detection_handler.process)
    telegram_service.connect()
