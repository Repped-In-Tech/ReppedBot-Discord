import discord

class AuthorizeButton(discord.ui.View):
    def __init__(self, url):
        super().__init__(timeout=30)
        button = discord.ui.Button(label='Unlock the goods!', style=discord.ButtonStyle.url, url=url)
        self.add_item(button)
