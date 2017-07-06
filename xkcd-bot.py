## xkcd-bot v2.0
## Author: Soma // Alicorn Industries
## !xkcd to summon current xkcd

## TODO: Add specific xkcd functionality

import discord
import urllib.request, json
from discord.ext.commands import Bot

# bot is a subclass of client
bot = Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_read():
    print('Client logged in')

@bot.command()
async def hello(*args):
    return await bot.say('Hello, world!')

@bot.command()
async def xkcd(*args):
    with urllib.request.urlopen('https://xkcd.com/info.0.json') as url:
        data = json.loads(url.read().decode())
        img_url = data['img']
    await bot.say(img_url)    

# Token here
bot.run('MzMyNTY4Nzc4ODgzNzI3Mzkw.DEAaQQ.gmM-Xs3MonYBjh7T-OG7iatw5Z8')
