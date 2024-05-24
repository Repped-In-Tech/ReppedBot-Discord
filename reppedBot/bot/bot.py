import requests
from discord.ext import commands
from reppedBot import BotConfigMixin
from .ui_components.button import AuthorizeButton
from .api import remove_member_from_db, update_user_roles_in_db

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
        remove_member_from_db(payload.user.id, self.remove_url)
    
    async def on_member_update(self, before, after):
        """
        sends the member id and roles to an external api for processing
        """
        update_user_roles_in_db(after.id, after.roles, self.update_url)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not recognized")
