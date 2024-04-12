from reppedBot import ReppedBot, initialize_commands

if __name__ == '__main__':
    bot = ReppedBot()
    initialize_commands(bot)
    bot.run(bot.discord_token)
