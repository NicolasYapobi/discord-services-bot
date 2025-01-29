import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from database import init_db, add_link, get_all_link

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!')

init_db()

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following serv:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@bot.command(name="list", help="Give a list of links")
async def on_message(ctx):
    all_link = get_all_link()
    await ctx.send(f"List of links: {all_link}")

@bot.command(name="add", help="Add a link in a topic\n'[TOPIC] link'")
async def on_message(ctx, topic = None, link = None):
    print(f"{topic} - {link}")
    if topic is None or link is None:
        await ctx.send(f"Wrong format, please enter a [TOPIC] with the link associated")
    else:
        add_link(topic, link)
        await ctx.send(f"Link added on [{topic}] topic")


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message:: {args[0]}\n')
        else: 
            raise


bot.run(TOKEN)
