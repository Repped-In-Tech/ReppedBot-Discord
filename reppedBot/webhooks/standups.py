import datetime
import time
import pytz
from discord import SyncWebhook
from reppedBot import BotConfigMixin

class StandupwWebhook(BotConfigMixin):

    def time_to_send_message(self):
        time_zone=pytz.timezone('America/Chicago')
        current_time = datetime.datetime.now(time_zone)
        if current_time.weekday() in [0,2,4] and current_time.hour == 12 and current_time.minute == 0:
            return True
        return False

    def send_message(self):
        print("I am running")
        while True:
            if self.time_to_send_message():
                webhook=SyncWebhook.from_url(self.webhook_url)
                webhook.send("This is a test")
            time.sleep(55)
