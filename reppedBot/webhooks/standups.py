import datetime
import time
import pytz
from discord import SyncWebhook
from reppedBot.config import BotConfigMixin

class StandupwWebhook(BotConfigMixin):

    def check_time(self):
        time_zone=pytz.timezone('America/Chicago')
        current_time = datetime.datetime.now(time_zone)
        if current_time.weekday() in [0,2,4] and current_time.hour == 14 and current_time.minute == 13:
            return True
        return False

    def send_message(self):
        print("I am running")
        while True:
            if self.check_time():
                webhook=SyncWebhook.from_url(self.webhook_url)
                webhook.send("This is a test")
            time.sleep(55)

if __name__ == '__main__':
    standup_messenger = StandupwWebhook()
    standup_messenger.send_message()
