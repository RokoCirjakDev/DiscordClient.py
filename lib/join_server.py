import requests
from lib.header import header

def join_server(bot: header,invite_link : str):
    invite_code = invite_link.split('/')[-1]
    
    url = f'https://discord.com/api/v9/invites/{invite_code}'

    # a diffrent header is needed for this request so bots header is not used
    joinserverheaders = {
        'Authorization': bot.get_auth_token(),
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=joinserverheaders)
    
    if response.status_code == 200:
        print('Successfully joined the server.')
    else:
        print(f'Failed to join the server: {response.status_code} - {response.json()}')