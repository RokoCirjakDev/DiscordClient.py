import requests
from lib.header import header

def get_servers(bot: header):
    url = 'https://discord.com/api/v9/users/@me/guilds'
    serverids = []
    # a diffrent header is needed for this request so bots header is not used
    headers = {
        'Authorization': bot.get_auth_token(),
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        servers = response.json()
        for server in servers:
            serverids.append(server['id'])
        return serverids
    else:
        print(f'Failed to get servers: {response.status_code} - {response.json()}')
        return None
