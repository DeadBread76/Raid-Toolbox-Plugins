import discord
import sys

token = sys.argv[1]
master = sys.argv[2]
client = discord.Client()

@client.event
async def on_message(message):
    copymaster = client.get_user(int(master))
    if message.author == copymaster:
        async with message.channel.typing():
            try:
                await message.channel.send(message.content)
            except Exception:
                pass

client.run(token,bot=False)
