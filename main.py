from nextcord.ext import commands; from nextcord import Intents; bot = commands.Bot(command_prefix=['?'], intents=Intents.all(), help_command=None); from os import listdir, environ
for fn in listdir('cogs'):  bot.load_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py') else print('not a python file')
bot.run(environ['token'])
