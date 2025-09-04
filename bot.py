#Install the required packages before running the bot:
import os
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
from jokeapi import Jokes

#This is the function that talks to JokeAPI to find a joke
async def get_jokes():
    j = await Jokes()
    joke = await j.get_joke(lang="en", blacklist=['nsfw', 'racist', 'sexist', 'explicit'])
    if joke["type"] == "single":
        return joke["joke"]
    else:
        return f'{joke["setup"]}\n{joke["delivery"]}'

#Make sure you have a .env file with your DISCORD_TOKEN variable set
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Set up the bot with the command prefix and intents
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

#This is the command that the bot will respond to
@bot.command(name='joke')
async def joke(ctx):
    response = await get_jokes()
    await ctx.send(response)

#Run the bot
bot.run(TOKEN)
