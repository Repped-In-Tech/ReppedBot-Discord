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

    @bot.command(name="getmembers")
    async def get_members(ctx):
        guild = bot.get_guild(bot.guild_id)
        members = guild.members
        member_list = [member.name for member in members]
        await ctx.send(f"Members in the guild {guild.name}:\n{', '.join(member_list)}")
