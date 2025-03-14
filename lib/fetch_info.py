from lib.header import header
from get_data import get_channel_data

def extract_one_message(response_data: dict, number: int):
    return response_data[number]

def get_mentions(message: dict):
    return message['mentions']

def get_type(message: dict):
    return message['type']

def get_content(message: dict):
    return message['content']

def get_mentions(message: dict):
    return message['mentions']

def get_mention_roles(message: dict):
    return message['mention_roles']

def get_attachments(message: dict):
    return message['attachments']

def get_embeds(message: dict):
    return message['embeds']

def get_timestamp(message: dict):
    return message['timestamp']

def get_edited_timestamp(message: dict):
    return message['edited_timestamp']

def get_flags(message: dict):
    return message['flags']

def get_components(message: dict):
    return message['components']

def get_id(message: dict):
    return message['id']

def get_channel_id(message: dict):
    return message['channel_id']

def get_author(message: dict):
    return message['author']

def get_pinned(message: dict):
    return message['pinned']

def get_author_id(message: dict):
    return message['author']['id']

def get_author_username(message: dict):
    return message['author']['username']

def get_author_avatar(message: dict):
    return message['author']['avatar']

def get_author_discriminator(message: dict):
    return message['author']['discriminator']

def get_author_public_flags(message: dict):
    return message['author']['public_flags']

def get_author_flags(message: dict):
    return message['author']['flags']

def get_author_banner(message: dict):
    return message['author']['banner']

def get_author_accent_color(message: dict):
    return message['author']['accent_color']

def get_author_global_name(message: dict):
    return message['author']['global_name']

def get_author_avatar_decoration_data(message: dict):
    return message['author']['avatar_decoration_data']

def get_author_banner_color(message: dict):
    return message['author']['banner_color']

def get_author_clan(message: dict):
    return message['author']['clan']

def get_author_primary_guild(message: dict):
    return message['author']['primary_guild']

def get_mention_everyone(message: dict):
    return message['mention_everyone']

def get_tts(message: dict):
    return message['tts']