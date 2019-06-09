from discord.ext.commands import Bot
from discord import Game
import random
import requests
import asyncio

TOKEN = #INSERT DISCORD BOT TOKEN HERE
BOT_PREFIX = ("?")


client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with hot ladies"))
    print("Logged in as "+client.user.name)

@client.command()
async def bitcoin():
    url ="http://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    value = response.json()["bpi"]["USD"]["rate"]
    await client.say("BTC price is $"+value)

@client.command()
async def coinflip(name = "Coinflip",descripion = "Flips a fair coin Heads/Tails",brief = "Flips a fair coin Heads/Tails"):
    randomnumber = random.randint(0,1)
    if randomnumber == 0:
        randomnumber = "Heads"
    else:
        randomnumber = "Tails"
    await client.say(randomnumber)
    
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(3600)

client.loop.create_task(list_servers())
    
client.run(TOKEN)
