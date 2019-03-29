import discord
import requests
import random
import sys

token = sys.argv[1]
chan = sys.argv[2]
client = discord.Client()
list = requests.get('http://www.bannedwordlist.com/lists/swearWords.txt').text.split("\n")

@client.event
async def on_ready():
    txtchan = client.get_channel(int(chan))
    while not client.is_closed():
        message = ''
        for x in range(5):
            message += random.choice(list).rstrip() + ' '
        await txtchan.send(message)
client.run(token, bot=False)
