import discord

import config

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

conf = config.Config()

client = MyClient(intents=intents, proxy=conf.get_proxy())
client.run(token=conf.get_token())