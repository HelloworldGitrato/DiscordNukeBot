import asyncio
import discord
from discord.ext import commands
import json


with open('config.json') as f:
    data = json.load(f)
key = data['Token']
active = data['ActiveName']
prefix = data['Prefix']

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents = intents, help_command=None)

@bot.event
async def on_ready():
    activity = discord.Game(name=active)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

async def main():
    async with bot:
        await bot.load_extension("Cogs.nuke")
        await bot.start(key)

asyncio.run(main())