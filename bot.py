# Needed Libraries

import discord
from discord import app_commands
from discord.ext import tasks
import asyncio
import sqlite

# Needed Variablen
from config import TOKEN
import globals
import IDs

# Intents

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Needed Methoden

@tree.command(name="edit-mc-name", description="Edit or put in your exact minecraft name to register for the oline-status-page-levae a blanket to delete your entry")
async def editname(interaction=discord.Interaction,mcname:str):
    if mcname=="":
        
    

@bot.event
async def on_member_join(member: discord.Member):
    member_id= member.id
    welcomechannel=bot.get_Channel(IDs.welcome_channel_id)
    welcomechannel.send(f"Hallo und Herzlich wilkommen <@{member_id}>! Dies ist dein Ort, um dich mit den anderen Mitgliedern auszutauschen, Handel zu betreiben, usw. Bitte füge auch deinen MC Namen mit /edit-mc-name hinzu, damit andere sehen können, ob du online bist.")
    # edit the Text of the welcome-message in the format wlcomechannel.send(f"place your text")
    # if you want to mention the user, just write <@{member_id}> directly into your text.

@bot.event
async def on_member_remove(member:discord.Member):
    welcomechannel=bot.get_Channel(IDs.welcome_channel_id)
    welcomechannel.send(f"Der User {member.name} hat uns leider verlassen! Wir wünschen ihm weiter alles Gute!)
    # here, you can also edit the leave-message by typing welcomechannel.send(f"put your text here")
    # to put the name of the user who left into this message, just write {member.name} into the text


@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot ist online als {bot.user.name}, die Commands sind synchronisiert!")
    globals.bot = bot

bot.run(TOKEN)
