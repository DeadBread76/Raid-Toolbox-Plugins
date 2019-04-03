# Plugin Author: DeadBread76
# Plugin Name: Random User Ping spammer
# Date: 03/04/2019

import discord
import random
import sys

client = discord.Client()
token = sys.argv[1]
SERVER = sys.argv[2]

@client.event
async def on_ready():
    server = client.get_guild(int(SERVER))
    channellist = []
    memberlist = []
    counter = random.randint(1, 10)
    while not client.is_closed():
        for member in server.members:
            memberlist.append(member)
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            channellist.append(channel)
        chan = random.choice(channellist)
        try:
            await chan.send(random.choice(memberlist).mention)
        except Exception:
            pass

client.run(token, bot=False)
