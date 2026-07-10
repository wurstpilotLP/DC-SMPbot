# Benötigte Libraries

import discord
from discord import app_commands
from discord.ext import tasks
import asyncio
import sqlite

# Benötigte Variablen
from config import TOKEN

# Intents

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Benötigte Methoden





@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot ist online als {bot.user.name}, die Commands sind synchronisiert!")

bot.run(TOKEN)