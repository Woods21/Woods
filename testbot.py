import discord

class MyClient(discord.client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
    	print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('ODkyMjgzNjU5NjI3OTQ2MDI3.YVKp6g.TUw05k5E-HOaKXbyA908DrYWLeQ')