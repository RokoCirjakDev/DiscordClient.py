import json
from sys import stderr
from http.client import HTTPSConnection
from lib.connect import get_connection;
from lib.header import header

def send_message(bot: header, message: str):
    try:
        header_data=bot.get_header()
        message_data = {
        "content": message,
        "tts": False,
        }
        conn=get_connection()
        message_data = json.dumps(message_data)
        channel_id=bot.get_channel_ID()
        
        conn.request(
            "POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
        response = conn.getresponse()
        if response.status == 200:
            print("Message sent successfully")
        else:
            stderr.write(f"Failed to send message, status: {response.status}, reason: {response.reason}\n")
            stderr.write(f"Response: {response.read().decode('utf-8')}\n")
    except Exception as e:
        stderr.write(f"Failed to send_message: {e}\n")
