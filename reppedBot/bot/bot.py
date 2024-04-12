import discord
from discord.ext import commands
from reppedBot import BotConfigMixin

class ReppedBot(BotConfigMixin, commands.Bot):
    """
    base class to interact with Discord server. Event listeners are defined within the class, commands are defined separately. 
    """
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        command_prefix = '!'
        super().__init__(intents=intents, command_prefix=command_prefix)

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, you successfully joined my test server for ReppedBot!'
        )
        
    

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not recognized")
    