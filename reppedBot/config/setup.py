import os
from dotenv import load_dotenv

class BotConfigMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.discord_token=os.getenv('DISCORD_TOKEN')
        self.webhook_url=os.getenv('WEBHOOK_URL')
