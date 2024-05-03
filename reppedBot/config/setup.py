import os
from dotenv import load_dotenv
import discord

class BotConfigMixin:
    """loader for environment variables for ReppedBot"""
    def __init__(self):
        load_dotenv()
        self.discord_token=os.getenv('DISCORD_TOKEN')

        self.guild_id=os.getenv('GUILD_ID')
        self.command_prefix=os.getenv('COMMAND_PREFIX')
        intents = discord.Intents.default()
        for intent in os.getenv('INTENTS').split(','):
            if hasattr(intents, intent):
                setattr(intents, intent, True)
        super().__init__(command_prefix=self.command_prefix, intents=intents)

class WebhookConfigMixin:
    """loader for environment variables for Webhook"""
    def __init__(self):
        load_dotenv()
        self.discord_token=os.getenv('DISCORD_TOKEN')
        self.webhook_url=os.getenv('WEBHOOK_URL')
