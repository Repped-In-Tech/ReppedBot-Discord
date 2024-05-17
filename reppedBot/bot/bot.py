import requests
from discord.ext import commands
from reppedBot import BotConfigMixin
from .button import AuthorizeButton

class ReppedBot(BotConfigMixin, commands.Bot):
    """
    base class to interact with Discord server. Event listeners are defined within the class, commands are defined separately. 
    """

    async def on_member_join(self, member):
        """
        sends a welcome message via DM when a member joins a server, and prompts to authorize with Oauth
        """
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, in order to access all the features of {member.guild.name}, click this button!',
            view=AuthorizeButton(self.auth_url)
        )

    async def on_raw_member_remove(self, payload):
        """
        sends the member id to an external api to sync info about leaving the server
        """
        requests.request(method='GET', url=self.remove_url, params={"member_id": payload.user.id}, timeout=3)
        
        

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not recognized")
