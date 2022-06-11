from nextcord.ext import commands
from ping_message import ping_message
from utils import add_role
import requests
from os import environ
class Ready(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def Ready(self):
    print('online')
    guild = self.bot.get_guild(978859818511110154)
    await guild.get_channel(984958731693482065).purge(limit=2)
    for member in guild.members:
      if 978860094932529214 not in [role.id for role in member.roles] and member.bot is False: add_role(978859818511110154, member.id, 978860094932529214)
    payload: dict = {
      'content': 'Jeg er pålogget'
    }
    requests.post(f'https://discord.com/api/v10/channels/985020834320105522/messages', headers={'authorization': 'Bot ' + environ['token']}, data=payload)
    await ping_message(self.bot)

  @commands.Cog.listener('on_member_join')
  async def join(self, member):
    add_role(978859818511110154, member.id, 978860094932529214)

def setup(bot):
  bot.add_cog(Ready(bot))
