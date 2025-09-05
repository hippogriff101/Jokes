import os
import discord
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
from jokeapi import Jokes

async def get_jokes():
    j = await Jokes()
    joke = await j.get_joke(lang="en", blacklist=['nsfw', 'racist', 'sexist', 'explicit'])
    if joke["type"] == "single":
        return joke["joke"]
    else:
        return f'{joke["setup"]}\n{joke["delivery"]}'

# Load token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents & bot
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

#  Legacy command
@bot.command(name="joke")
async def joke_prefix(ctx):
    response = await get_jokes()
    await ctx.send(response)

# Slash command
@bot.tree.command(name="joke", description="Get a random joke")
async def joke_slash(interaction: discord.Interaction):
    response = await get_jokes()
    await interaction.response.send_message(response)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
