import discord
from Thesaurusise import synonymise_sentance

token = "NDUwMzM4MTIxMDA4MTUyNTg3.YlJ-BA.ysbTZZJOih_dnNzudWNHR6__XeE"

client = discord.Client()


@client.event
async def on_message(message):
    if message.author != client.user:
        return
    content  = message.content.split(' ')
    content = synonymise_sentance(content)
    await message.edit(content=content)

client.run(token, bot=False)