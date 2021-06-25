import discord
import os
from dotenv import load_dotenv
from random_talents import roll_talents

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "$roll":
        result = roll_talents()
        await message.author.send(result)


@client.event
async def on_connect():
    print("bot connected to the server!")


client.run(TOKEN)
