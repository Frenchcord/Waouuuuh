import nextcord
from log import logging
class ticket_buttons(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="ticket", style = nextcord.ButtonStyle.green)
  async def confirm(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    view = cbtn()
    await interaction.response.send_message('Es-tu sure de vouloir faire cela?', view=view, ephemeral=True)
    await view.wait()

class cbtn(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="Oui", style = nextcord.ButtonStyle.green)
  async def Oui(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    for channel in interaction.guild.channels:
      if channel.name == f'ticket-{interaction.user.id}':
        await interaction.response.send_message(f'Tu as déja un ticket.\n{channel.mention}', ephemeral=True)
        return
    channel = await interaction.guild.create_text_channel(f'ticket-{interaction.user.id}', category=interaction.guild.get_channel(987814051885240330))
    await channel.set_permissions(interaction.user, send_messages=True, read_messages=True)
    await interaction.response.send_message(f'{channel.mention}', ephemeral=True)
    msg = await channel.send('@everyone')
    await msg.delete()
    await channel.send(embed=nextcord.Embed(title=f'Le staff sera bientot la {interaction.user.name} !', color = 0x2ecc71))
    logging(f'{interaction.user} vien de faire un ticket  ({channel.mention})')

  @nextcord.ui.button(label="Non", style = nextcord.ButtonStyle.red)
  async def Non(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    await interaction.response.send_message("Demande annulée!", ephemeral=True)
    logging(f'{interaction.user} a ésiter à faire un ticket ou a missclick')
