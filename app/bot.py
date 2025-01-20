import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')
print(GUILD)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following serv:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return
    if message.content == "Hey":
        response = "Oh ! Got in touch"
        await message.channel.send(response)
    

client.run(TOKEN)
