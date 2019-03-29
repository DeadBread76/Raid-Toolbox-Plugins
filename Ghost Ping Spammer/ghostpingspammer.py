# Plugin Author: DeadBread76
# Plugin Name: Ghost Ping Spammer
# Date: 29/03/2019

import discord
import asyncio
import random
import sys

token = sys.argv[1]
SERVER = sys.argv[2]
client = discord.Client()


@client.event
async def on_ready():
    server = client.get_guild(int(SERVER))
    channellist = []
    counter = random.randint(1, 10)
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            channellist.append(channel)
        chan = random.choice(channellist)
        try:
            await chan.send('@everyone')
        except Exception:
            pass
        await asyncio.sleep(int(counter))


@client.event
async def on_message(message):
    if message.author == client.user:
        if message.content == '@everyone':
            await message.delete()
    else:
        pass

client.run(token, bot=False)
