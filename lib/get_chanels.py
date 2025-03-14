import requests
from lib.header import header

def get_channels(bot:header, server_id):
    url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
    channelIds = []
    # a diffrent header is needed for this request so bots header is not used
    headers = {
        'Authorization': bot.get_auth_token(),
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        channels = response.json()
        for channel in channels:
            channelIds.append(channel['id'])
        return channelIds
    else:
        print(f'Failed to get channels: {response.status_code} - {response.json()}')
        return None

