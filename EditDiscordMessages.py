import discord
from Thesaurusise import synonymise_sentance
import os

if os.path.exists('token.txt'):
    with open('token.txt') as f:
        token = f.read().strip()
else:
    token = input('Enter token: ')
    with open('token.txt', 'w') as f:
        f.write(token)

client = discord.Client()


@client.event
async def on_message(message):
    if message.author != client.user:
        return
    content  = message.content.split(' ')
    content = synonymise_sentance(content)
    await message.edit(content=content)

client.run(token, bot=False)
