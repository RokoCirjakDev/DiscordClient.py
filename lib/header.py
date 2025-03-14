class header:
    def __init__(self, auth_token):
        self.auth_token = auth_token
    def generate_header(self, channel_url):
        self.channel_URL = channel_url
        self.header_data = {
            "Content-Type": "application/json",
            "Authorization": self.auth_token,
            "Host": "discordapp.com",
            "Referer": self.channel_URL
        }
        self.channel_ID = self.channel_URL.split("/")[-1]
    
    def generate_header_from_username(self, username):
        self.header_data = {
            "Content-Type": "application/json",
            "Authorization": self.auth_token,
            "Host": "discordapp.com",
            "Referer": f"https://discordapp.com/channels/@me/{username}"
        }

    def get_channel_ID(self):
        return self.channel_ID
    def get_header(self):
        if self.header_data == None:
            raise Exception("Header data not generated")
        return self.header_data
    def get_auth_token(self):
        return self.auth_token
    def get_channel_URL(self):
        return self.channel_URL
    def set_auth_token(self, auth_token):
        self.auth_token = auth_token