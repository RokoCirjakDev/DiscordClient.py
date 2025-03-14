from sys import stderr
import json
from lib.header import header
from lib.get_data import get_channel_data
from lib.connect import get_connection

def fetch_last_messages(bot, channel_id, number):
    i = 0
    messagescontent = []

    response_data = get_channel_data(bot, channel_id, number)
        
    try:
            messages = json.loads(response_data)
            for message in messages:
              messagescontent.append(message['content'])
            return messagescontent
    except json.JSONDecodeError:
            stderr.write("Failed to parse JSON response\n")
            return None
    
def fetch_last_message(bot, channel_id):
    messages = fetch_last_messages(bot, channel_id, 1)
    if messages:
        return messages[0]
    else:
        return None
    
def fetch_messages_and_time(bot, channel_id):
    messages = fetch_last_messages(bot, channel_id, 100)
    if messages:
        return messages
    else:
        return None