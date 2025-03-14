import requests
from sys import stderr
import json
from lib.connect import get_connection
from lib.header import header

def send_friend_request(bot: header, friend_username: str):
    try:
        header_data=bot.get_header()
        data = {
            "username": friend_username,
            "discriminator": 0
        }
        conn=get_connection()
        data = json.dumps(data)
        url = f"/api/v9/users/@me/relationships"
        
        conn.request(
            "POST", url, data, header_data)
        response = conn.getresponse()
        if response.status == 204:
            print("Friend request sent successfully")
        else:
            stderr.write(f"Failed to send friend request, status: {response.status}, reason: {response.reason}\n")
            stderr.write(f"Response: {response.read().decode('utf-8')}\n")
    except Exception as e:
        stderr.write(f"Failed to send_friend_request: {e}\n")