import datetime
import time
import pytz
from discord import SyncWebhook
from reppedBot import WebhookConfigMixin

class StandupwWebhook(WebhookConfigMixin):

    STANDUP_MESSAGE = "👋🏾 Reminder to send in your update before the end of your day!\n\n 🏆 Wins (what you’ve accomplished since last time) \n🗺️  Plan (what you plan on working on the next 1-2 days) \n⛔ Help Requested / Questions (how can we help you?)"

    def time_to_send_message(self):
        time_zone=pytz.timezone('America/Chicago')
        current_time = datetime.datetime.now(time_zone)
        if current_time.weekday() in [0,2,4] and current_time.hour == 12 and current_time.minute == 00:
            return True
        return False

    def send_message(self):
        print("I am running")
        while True:
            if self.time_to_send_message():
                webhook=SyncWebhook.from_url(self.webhook_url)
                webhook.send(self.STANDUP_MESSAGE)
            time.sleep(60)
