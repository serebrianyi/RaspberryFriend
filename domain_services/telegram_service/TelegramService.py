from commands.CommandFactory import CommandFactory
from commands.UnauthorizedCommand import UnauthorizedCommand
import requests
import time
import os
from domain_services.logging_service.LoggingService import LoggingService
requests.packages.urllib3.disable_warnings()

class TelegramService(object):

    offset = 0

    def __init__(self, configuration):
        self.configuration = configuration

    def _load_data(self):
        data = {'offset': self.offset + 1, 'limit': 5, 'timeout': 0}
        try:
            request = requests.post(self.configuration.url + self.configuration.token + '/getUpdates', data=data, timeout=1)
        except:
            LoggingService.info('Error getting updates')
            return []

        if not request.status_code == 200:
            LoggingService.info("Request failed with code " + str(request.status_code))
            return []
        LoggingService.info(request.json())
        if not request.json()['ok']: return []
        return request.json()['result']

    def check_updates(self, data):

        # Message gets accepted if
        # (1) Sender is authorized
        # (2) Correct recipient
        for update in data:
            self.offset = update['update_id']
            from_id = update['message']['chat']['id']
            name = update['message']['chat']['first_name']
            if from_id not in self.configuration.allowed_access:
                LoggingService.info("Unauthorized access")
                return self.send_text(from_id, UnauthorizedCommand(None).process(from_id))
                continue
            message = update['message']['text']
            parameters = (self.offset, name, from_id, message)
            LoggingService.info('Message (id%s) from %s (id%s): "%s"' % parameters)
            body = self.check_recipient_params(message)
            if body is None:
                LoggingService.info("Different recipient")
                continue
            command = CommandFactory.create_command(body)
            try:
                return_message = command.process(from_id)
                self.send_message(from_id, return_message)
            except Exception as inst:
                LoggingService.exception(inst)
                return self.send_text(from_id, str(inst))

    def send_message(self, from_id, return_message):
        if "photo_filename" in return_message:
            self.send_photo(from_id, return_message["photo_filename"])
        elif "video_filename" in return_message:
            self.send_video(from_id, return_message["video_filename"])
        else:
            self.send_text(from_id, return_message["message_text"])

    def send_text(self, chat_id, text):
        LoggingService.info('Sending to %s: %s' % (chat_id, text))
        data = {'chat_id': chat_id, 'text': "(" + self.configuration.pi_name + ")" + os.linesep +text}
        request = requests.post(self.configuration.url + self.configuration.token + '/sendMessage', data=data)
        if not request.status_code == 200:
            return False
        return request.json()['ok']

    def send_photo(self, chat_id, file_name):
        LoggingService.info('Sending to %s: %s' % (chat_id, file_name))
        data = {'chat_id': chat_id}
        files = {'photo': open(file_name, 'rb')}
        request = requests.post(self.configuration.url + self.configuration.token + '/sendPhoto', data=data, files=files)
        return request.json()['ok']

    def send_video(self, chat_id, file_name):
        LoggingService.info('Sending to %s: %s' % (chat_id, file_name))
        data = {'chat_id': chat_id}
        files = {'document': open(file_name, 'rb')}
        request = requests.post(self.configuration.url + self.configuration.token + '/sendDocument', data=data, files=files)
        return request.json()['ok']

    def connect(self):
        while True:
            LoggingService.info('while True')
            try:
                LoggingService.info('self.check_updates(self._load_data())')
                self.check_updates(self._load_data())
                LoggingService.info('time.sleep(self.configuration.interval)')
                time.sleep(self.configuration.interval)
            except KeyboardInterrupt:
                break
        LoggingService.info('EXIT')

    def send_to_all(self, msg):
        for recipient in self.configuration.allowed_access:
            self.send_message(recipient, msg)

    def check_recipient_params(self, params):
        first_param = params.strip().find(" ")
        if first_param > -1:
            pi_name = params[:first_param].lower()
            if pi_name == self.configuration.pi_name:
                return params[first_param:].strip()
            else:
                if self.configuration.is_master and pi_name not in self.configuration.slaves:
                    return params
        else:
            if self.configuration.is_master:
                return params