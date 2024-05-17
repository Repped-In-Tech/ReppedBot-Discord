from discord.utils import get
from .data import ROLE_IDS

def initialize_commands(bot):
    """function that takes an instance of a bot and adds commands to the bot"""

    @bot.command(name="hello")
    async def say_hey(ctx):
        """bot responds with 'HEY' when !hello is input in Discord"""
        response = 'HEY'
        await ctx.send(response)

    @bot.command(name="saymyname")
    async def say_my_name(ctx):
        response = f'What up {ctx.author}'
        await ctx.send(response)

    @bot.command(name="superstar")
    async def add_superstar_role(ctx):
        author = ctx.author
        role = get(ctx.guild.roles, id=ROLE_IDS["Superstar"])
        await author.add_roles(role)
        await ctx.send("role added!")

    @bot.command(name="email")
    async def save_email(ctx, email=None):
        if email:
            print(email)
            await ctx.send("Thanks for signing up!")
        else:
            await ctx.send("please send a valid email")
