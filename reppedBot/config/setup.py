import os
from dotenv import load_dotenv

class BotConfig:
    def __init__(self):
        load_dotenv()
        self.discord_token=os.getenv('DISCORD_TOKEN')
        self.webhook_url=os.getenv('WEBHOOK_URL')
