from nextcord.ext import commands
from random import randint
funfactlist: list = [
  'Ce module s\'est fait faire parce que les modules existant sont pas opti',
  'Ce module s\'est fait coder par un clavier à 20 $',
  'L\'un des devs à appris à coder en même temps de coder Frenchcord',
  'Le bot Waouuuh est fait avec nextcord',
  'La database de Frenchcord est Namedb (https://github.com/Name-shitty-github-profile/namedb) recopier (ctrl + c ctrl + v)',
  'Le nom du mini module zaza s\'est fait nommer ainsi à cause de la mort du chat de la créatrice (zaza)',
  'La créatrice déteste une partie des modules existants pour discord api'
]

class Funfact(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def funfact(self, ctx):
    await ctx.send(f'Fun fact : {funfactlist[randint(0, len(funfactlist))]}')

def setup(bot):
  bot.add_cog(Funfact(bot))
