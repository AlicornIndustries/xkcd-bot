## XKCD-bot v1.0
## Author: Soma // Alicorn Industries
## !xkcd to summon current XKCD

####### DON'T FORGET TO PUT YOUR CLIENT ID IN YOUR_CLIENT_ID_HERE

import discord
import asyncio
import urllib.request, json

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!xkcd"):
        # Get current XKCD
        with urllib.request.urlopen('https://xkcd.com/info.0.json') as url:
            data = json.loads(url.read().decode())
            img_url = data['img']
        await client.send_message(message.channel, img_url)
        
client.run("YOUR_CLIENT_ID_HERE")
