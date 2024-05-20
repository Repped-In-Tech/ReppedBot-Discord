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
        self.auth_url = os.getenv('AUTHORIZATION_URL')
        self.remove_url = os.getenv('API_REMOVE_ENDPOINT')
        self.update_url = os.getenv('API_UPDATE_ROLES_ENDPOINT')
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
        self.standup_message=os.getenv('STANDUP_MESSAGE')
