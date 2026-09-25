# Needed Libraries
from asyncio import tasks
from typing import cast
import discord
import os
import dotenv
from discord import Client

# Needed Variables and constants

import IDs
import globals
import embeds

# Needed methods
from db_config import init_db
import db_requests
import mcrequests

# Intents

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot: Client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)
dotenv.load_dotenv()


# Needed Methods

@tree.command(name="edit-mc-name",
              description="Edit or put in your exact minecraft name to register for the oline-status-page-levae a blanket to delete your entry")
async def editname(interaction: discord.Interaction, mcname: str):
    answer = db_requests.change_mcname(mcname)
    if answer == True:
        await interaction.response.send_message(f"The Minecraft name {mcname} was successfully updated!")
    else:
        await interaction.response.send_message("There is no valid Minecraft name!")


@bot.event
async def on_member_join(member: discord.Member):
    welcome_channel = bot.get_channel(IDs.welcome_channel_id)
    await welcome_channel.send(
        f"Hallo und Herzlich wilkommen <@{member.id}>! Dies ist dein Ort, um dich mit den anderen Mitgliedern auszutauschen, Handel zu betreiben, usw. Bitte füge auch deinen MC Namen mit /edit-mc-name hinzu, damit andere sehen können, ob du online bist.")

    service_channel = bot.get_channel(IDs.service_channel_id)

    if await db_requests.new_member_entry(member.id):
        await service_channel.send(f"The User {member.name} was added successfully!")
    else:
        await service_channel.send(f"The User {member.name} already existed in the database! Please contact the support!")

# region userverlassen
@bot.event
async def on_member_remove(member: discord.Member):
    welcome_channel = bot.get_Channel(IDs.welcome_channel_id)
    service_channel = bot.get_channel(IDs.service_channel_id)
    await welcome_channel.send(f"Unfortunately, the user {member.name} left us! We wish him all the best for the future!")
    if await db_requests.delete_member(member.id):
        await service_channel.send(f"The User {member.name} was deleted successfully!")
    else:
        await service_channel.send(f"The User {member.name} never existed in the database! please contact support!")
# endregion

@bot.event
async def on_ready():
    await init_db()
    await tree.sync()
    print(f"Bot is online as {bot.user.name}, commands are synchronised")
    globals.bot = bot

@tasks.loop(minutes=5)
async def abfrage_online_player():
    online_members = await mcrequests.request_member_status()
    if online_members:

        embed = embeds.get_online_members_embed(online_members)

    else:

        embed = embeds.get_no_online_members_embed()

    activity_channel = cast(discord.TextChannel, bot.get_channel(IDs.activity_channel_id))

    await activity_channel.purge(limit = None)

    await activity_channel.send(embed=embed) # type: ignore

bot.run(os.getenv("TOKEN"))
