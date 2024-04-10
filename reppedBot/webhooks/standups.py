import datetime
import time
import pytz
from discord import SyncWebhook
from reppedBot.config import BotConfig

class StandupwWebhook(BotConfig):

    def check_time(self):
        time_zone=pytz.timezone('America/Chicago')
        current_time = datetime.datetime.now(time_zone)
        if current_time.weekday() in [0,2,4] and current_time.hour == 14 and current_time.minute == 41:
            return True
        return False

    def send_message(self):
        while True:
            if self.check_time():
                webhook=SyncWebhook.from_url(self.webhook_url)
                webhook.send("This is a test")
            time.sleep(55)
