import discord
from discord.ext import commands
from reppedBot import BotConfigMixin

class ReppedBot(BotConfigMixin, commands.Bot):
    def __init__(self,):
        intents = discord.Intents.default()
        intents.message_content = True
        command_prefix = '!'
        super().__init__(intents=intents, command_prefix=command_prefix)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(error)
    