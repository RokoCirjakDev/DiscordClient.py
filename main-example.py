from lib.header import header
from lib.send_msg import send_message
from lib.get_data import get_channel_data
from lib.fetch_message import fetch_last_message, fetch_last_messages
from lib.fetch_info import (
    extract_one_message,get_type, get_content, get_mentions, get_mention_roles, get_attachments,
    get_embeds, get_timestamp, get_edited_timestamp, get_flags, get_components,
    get_id, get_channel_id, get_author, get_pinned, get_mention_everyone, get_tts
)
from lib.send_friend_request import send_friend_request
from lib.join_server import join_server

auth_token = 'your_token_here'

if __name__ == "__main__":
    # declare account for header creation
    bot1 = header(auth_token)
    
    channel_URL = 'chat_url_here' # this is the URL of the MAIN channel you want to send messages to
    # generate header (bot1 can now send messages to the channel), run generate header again to change channel
    bot1.generate_header(channel_URL) 

    channel_id = bot1.get_channel_ID()
    
    # Send a message
    send_message(bot1,  "Hello World")
    
    # Fetch channel data
    response_data = get_channel_data(bot1, 1)

    #extract one message from response data
    print(extract_one_message(response_data, 0))
    
    # Fetch the last message
    last_message = fetch_last_message(bot1, channel_id)

    # print message
    print(last_message.read().decode('utf-8'))

    # Fetch the last 10 messages
    last_messages = fetch_last_messages(bot1, channel_id, 10)
    
    Username = "target_account_username"
    # send friend request
    send_friend_request(bot1, Username)

    # generate header from username (bot now sends to target account instead of a server channel)
    bot1.generate_header_from_username(Username)

    # bot1 joins server
    invite_link = "invite_link_here"
    join_server(bot1, invite_link)

    
    # Extract information from message
    print("Type:", get_type(last_message))
    print("Content:", get_content(last_message))
    print("Mentions:", get_mentions(last_message))
    print("Mention Roles:", get_mention_roles(last_message))
    print("Attachments:", get_attachments(last_message))
    print("Embeds:", get_embeds(last_message))
    print("Timestamp:", get_timestamp(last_message))
    print("Edited Timestamp:", get_edited_timestamp(last_message))
    print("Flags:", get_flags(last_message))
    print("Components:", get_components(last_message))
    print("ID:", get_id(last_message))
    print("Channel ID:", get_channel_id(last_message))
    print("Author:", get_author(last_message))
    print("Pinned:", get_pinned(last_message))
    print("Mention Everyone:", get_mention_everyone(last_message))
    print("TTS:", get_tts(last_message))