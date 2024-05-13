from discord.ext import commands
from reppedBot import BotConfigMixin
from .data import ROLE_IDS

class ReppedBot(BotConfigMixin, commands.Bot):
    """
    base class to interact with Discord server. Event listeners are defined within the class, commands are defined separately. 
    """

    async def on_member_join(self, member):
        """
        sends a welcome message via DM when a member joins a server
        """
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, you successfully joined {member.guild.name}!'
        )
    

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not recognized")
