# bot.py
import os
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
from jokeapi import Jokes

# Make get_jokes an async function
async def get_jokes():
    j = await Jokes()
    joke = await j.get_joke(lang="en", blacklist=['nsfw', 'racist', 'sexist', 'explicit'])
    if joke["type"] == "single":
        return joke["joke"]
    else:
        return f'{joke["setup"]}\n{joke["delivery"]}'

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up bot
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='joke')
async def joke(ctx):
    response = await get_jokes()
    await ctx.send(response)

# Run bot
bot.run(TOKEN)
