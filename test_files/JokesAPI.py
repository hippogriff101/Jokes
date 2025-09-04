from jokeapi import Jokes
import asyncio

async def print_joke():
    j = await Jokes()
    joke = await j.get_joke(lang="en", blacklist=['nsfw', 'racist', 'sexist', 'explicit'])
    if joke["type"] == "single":
        print(joke["joke"])
    else:
        print(joke["setup"])
        print(joke["delivery"])

asyncio.run(print_joke())