import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following serv:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
@bot.command(name="list", help="Give a list of links")
async def on_message(ctx):
    response = "List of links:"
    await ctx.send(response)
    
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message:: {args[0]}\n')
        else: 
            raise


bot.run(TOKEN)
