import discord #akan mengimport modul discord
import os # akan mengimport osmo

client = discord.Client()

@client.event # bagian ini akan memberitahu kalau bot sudah on
async def on_ready():
    print("I'm in")
    print(client.user) # client user adalah bot kita

@client.event # bagian ini adalah ketika orang mengetik sesuatu di maka outputnya akan terbalik
async def on_message(message):
    if message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])

token = os.environ.get("DISCORD_BOT_SECRET")
client.run("token")
