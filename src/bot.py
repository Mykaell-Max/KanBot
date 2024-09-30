import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from commands import setup_commands

intents = discord.Intents.all()
intents.members = True

load_dotenv()
TOKEN = os.getenv('BOTTOKEN')

KanBot = commands.Bot(command_prefix='k!', intents=intents)

setup_commands(KanBot)

@KanBot.event
async def on_ready():
    channel = KanBot.get_channel(1290297651614449769)
    online = discord.Embed(
        title='KanBot ONLINE',
        color=discord.Color.light_embed(),
        description=f'{KanBot.user} is connected!'
    )
    await channel.send(embed=online)

KanBot.run(TOKEN)