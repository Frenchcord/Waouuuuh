import nextcord
class ping_buttons(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="update", style = nextcord.ButtonStyle.gray)
  async def update(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    role = interaction.guild.get_role(984999472268443648)
    if 984999472268443648 in [role.id for role in interaction.user.roles]:
      await interaction.user.remove_roles(role)
    else:
      await interaction.user.add_roles(role)

  @nextcord.ui.button(label="daily update", style = nextcord.ButtonStyle.gray)
  async def daily(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    role = interaction.guild.get_role(984999531307466823)
    if 984999531307466823 in [role.id for role in interaction.user.roles]:
      await interaction.user.remove_roles(role)
    else:
      await interaction.user.add_roles(role)

  @nextcord.ui.button(label="alpha tester", style = nextcord.ButtonStyle.gray)
  async def alpha(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    role = interaction.guild.get_role(984999569223974993)
    if 984999569223974993 in [role.id for role in interaction.user.roles]:
      await interaction.user.remove_roles(role)
    else:
      await interaction.user.add_roles(role)
  
async def ping_message(bot):
  view = ping_buttons()
  rolecont: str = ''
  rolelist: list = [
    {"name": "Update ping", "desc": "Vous allez vous faire ping, pour les grosses updates de Frenchcord."},
    {"name": "Daily update", "desc": "Vous allez vous faire ping chaque jour, pour chaque daily update."},
    {"name": "Alpha tester", "desc": "\"Un og ticket\"\nVous allez vous faire pings à chaque update de version, Alpha (0.0.1 jusqu'à 1.0.0)"}
  ]
  for i in rolelist: rolecont += f"\n**{i['name']}**\n{i['desc']}"
  await bot.get_guild(978859818511110154).get_channel(984958731693482065).send(embed = nextcord.Embed(title='Roles_ping', description=f"Cliquez le boutton pour le role que vous voulez\n**Roles info**\n {rolecont}"), view=view)
  await NameSend(bot)
  await view.wait()

async def NameSend(bot):
  webook = await bot.get_guild(978859818511110154).get_channel(984958731693482065).create_webhook(name='Name')
  name = await bot.fetch_user(884220029867003916)
  await webook.send('Veuillez prendre note que les pings vont changer et donc certains roles vont plus être là bientôt', avatar_url=name.avatar.url)
  await webook.delete()
