import Adafruit_DHT


class TempHandler(object):

    def process(self, model, pin):
        humidity, temperature = self._get_temp(model, pin)
        if humidity is not None and temperature is not None:
            return {"message_text": 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)}
        else:
            return {"message_text": 'Failed to get reading. Try again!'}

    def _get_temp(self, model, pin):
        return Adafruit_DHT.read_retry(model, pin)


