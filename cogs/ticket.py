from nextcord.ext import commands
from utils import namesend
from nextcord import Embed
from ticketbtn import ticket_buttons
class Ticket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def Readye(self):
    channel = self.bot.get_guild(978859818511110154).get_channel(987745737649565727)
    await channel.purge(limit=2)
    view = ticket_buttons()
    await channel.send(embed=Embed(title="Ticket", description='Veuillez cliquer sur le boutton "ticket" pour créer un ticket'), view=view)
    await namesend(self.bot, 'Veuillez prendre note que tout ticket inutile sera sanctionné.', channel)
    await view.wait()

  @commands.command()
  async def close(self, ctx):
    if ctx.author.id != 884220029867003916: return
    if not ctx.channel.name.startswith("ticket"): return
    await ctx.send('Laisse moi analyser tout cela avant ...')
    msglist = []
    async for message in ctx.channel.history(limit = 100): msglist.append(message)
    await ctx.channel.delete()
    channel = await ctx.guild.create_text_channel(f'archive-{ctx.channel.name}', category=ctx.guild.get_channel(987818519804674048))
    msglist.reverse()
    for message in msglist: await channel.send(embed=Embed(title=f'{message.author}', description=message.content, color = 0xe91e63).set_footer(text=message.created_at.__format__('%A, %d. %B %Y %H:%M:%S')))

def setup(bot):
  bot.add_cog(Ticket(bot))
