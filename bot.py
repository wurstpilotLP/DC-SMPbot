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

@tree.command(name="edit-mc-name", description="Edit or put in your exact minecraft name to register for the oline-status-page-levae a blanket to delete your entry")
async def editname(interaction=discord.Interaction,mcname:str):
    if mcname=="":
        
    



@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot ist online als {bot.user.name}, die Commands sind synchronisiert!")

bot.run(TOKEN)
