import requests
from lib.header import header
def get_usernames_from_server(bot:header, server_id: str, number: int):
    url = f'https://discord.com/api/v9/guilds/{server_id}/members'
    usernames = []
    # a diffrent header is needed for this request so bots header is not used
    headers = {
        'Authorization': bot.get_auth_token(),
        'Content-Type': 'application/json'
    }
    
    params = {
        'limit': number # Number of members to get
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        members = response.json()
        for member in members:
            usernames.append(member['user']['username'])
        return usernames
    else:
        print(f'Failed to get members: {response.status_code} - {response.json()}')
        return None
