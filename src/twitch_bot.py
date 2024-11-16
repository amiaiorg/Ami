import os
import requests
from twitchio.ext import commands

# Twitch Bot Configuration
TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_CHANNEL = os.getenv('TWITCH_CHANNEL')

# Eggdrop Bot Configuration
EGGDROP_URL = os.getenv('EGGDROP_URL')
EGGDROP_API_KEY = os.getenv('EGGDROP_API_KEY')

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TWITCH_TOKEN, client_id=TWITCH_CLIENT_ID, prefix='!', initial_channels=[TWITCH_CHANNEL])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='moderate')
    async def moderate(self, ctx, *, message):
        response = self.send_to_eggdrop(message)
        await ctx.send(response)

    def send_to_eggdrop(self, message):
        payload = {
            'api_key': EGGDROP_API_KEY,
            'message': message
        }
        response = requests.post(EGGDROP_URL, json=payload)
        if response.status_code == 200:
            return 'Message sent to Eggdrop bot successfully.'
        else:
            return 'Failed to send message to Eggdrop bot.'

if __name__ == "__main__":
    bot = Bot()
    bot.run()