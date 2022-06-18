import requests; from os import environ
def logging(content: str):
  requests.post(f'https://discord.com/api/v10/channels/985020834320105522/messages', headers={'authorization': 'Bot ' + environ['token']}, data={'content': content})
