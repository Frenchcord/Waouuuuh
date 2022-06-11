from nextcord.ext import commands
from ping_message import ping_message

class Ready(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def Ready(self):
    print('online')
    guild = self.bot.get_guild(978859818511110154)
    await guild.get_channel(984958731693482065).purge(limit=2)
    for member in guild.members:
      if 978860094932529214 not in [role.id for role in member.roles] and member.bot is False: await member.add_roles(guild.get_role(978860094932529214))
    await guild.get_channel(985020834320105522).send('Jeg er pålogget') # Norwegian ❤️
    await ping_message(self.bot)

def setup(bot):
  bot.add_cog(Ready(bot))
