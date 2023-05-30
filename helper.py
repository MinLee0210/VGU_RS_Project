import random
import time
import  sys
from  Adafruit_IO import  MQTTClient


    
class AccessAdafruit:
    def __init__(self, username, key):
        AIO_USERNAME = username
        AIO_KEY = key
        self.client = MQTTClient(AIO_USERNAME , AIO_KEY)

    def run(self):
        self.client.connect()
        self.client.loop_background()
        time.sleep(5)

        while True:
            value = random.randint(0, 100)
            self.client.publish("your_feed", value)
            time.sleep(30)