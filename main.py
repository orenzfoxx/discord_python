import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])

token = os.environ.get("DISCORD_BOT_SECRET")
client.run("NTUyMTA4ODM3MTYzNzYxNjY1.D2V-YQ.e0axw603axrT3-Etuga3XqFuN74")
