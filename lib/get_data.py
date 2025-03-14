from lib.connect import get_connection
from lib.header import header
import json

def get_channel_data(bot :header, number: int):
    conn = get_connection()
    channel_ID = bot.get_channel_ID()
    conn.request(
        "GET", f"/api/v6/channels/{channel_ID}/messages?limit={number}", headers=bot.get_header())
    response = conn.getresponse()
    response_data = json.loads(response.read().decode("utf-8"))
    return response_data

def get_channel_list_from_server(bot: header):
    conn = get_connection()
    conn.request(
        "GET", "/api/v6/users/@me/channels", headers=bot.get_header())
    response = conn.getresponse()
    response_data = json.loads(response.read().decode("utf-8"))
    return response_data