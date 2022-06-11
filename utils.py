import requests
from os import environ
url: str = 'https://discord.com/api/v10'
def add_role(guild_id, member_id, role_id):
  requests.put(f'{url}/guilds/{guild_id}/members/{member_id}/roles/{role_id}', headers={'authorization': 'Bot ' + environ['token']})
def rem_role(guild_id, member_id, role_id):
  requests.delete(f'{url}/guilds/{guild_id}/members/{member_id}/roles/{role_id}', headers={'authorization': 'Bot ' + environ['token']})
