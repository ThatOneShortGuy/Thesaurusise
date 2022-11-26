import discord
from Thesaurusise import synonymise_sentance

token = "Insert Your Discord Token Here!!!"

client = discord.Client()


@client.event
async def on_message(message):
    if message.author != client.user:
        return
    content  = message.content.split(' ')
    content = synonymise_sentance(content)
    await message.edit(content=content)

client.run(token, bot=False)
