# Needed Libraries
from asyncio import tasks
from typing import cast
import discord
import os
import dotenv
from discord import Client, app_commands
from discord.ext import tasks

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

#region admin_commands

@tree.command(name="delete-user-manual", description="Delete user manually.")
#@app_commands.checks.has_permissions(administrator=False)
async def delete_user_manual(interaction: discord.Interaction, member: discord.Member):
    service_channel = bot.get_channel(IDs.service_channel_id)
    userid = member.id
    if await db_requests.delete_member(userid):
        await service_channel.send(f"The User {member.name} was deleted successfully!")
        await interaction.response.send_message(f"The User {member.name} was deleted successfully!", ephemeral=True)
    else:
        await service_channel.send(f"The User {member.name} never existed in the database! please contact support!")
        await interaction.response.send_message(
            f"The User {member.name} never existed in the database! please contact support!", ephemeral=True)

@tree.command(name="add-user-manual", description="Add user manually.")
#@app_commands.checks.has_permissions(administrator=False)
async def add_user_manual(interaction: discord.Interaction, member: discord.Member):
    service_channel = bot.get_channel(IDs.service_channel_id)
    userid = member.id
    if await db_requests.new_member_entry(userid):
        await service_channel.send(f"The User {member.name} was added successfully!")
        await interaction.response.send_message(f"The User {member.name} was added successfully!", ephemeral=True)
    else:
        await service_channel.send(f"The User {member.name} already existed in the database! Please contact support!")
        await interaction.response.send_message(
            f"The User {member.name} already existed in the database! Please contact support!", ephemeral=True)

@tree.command(name="edit-name-manual", description="Edit the Minecraft name of another user.")
#@app_commands.checks.has_permissions(administrator=False)
async def edit_name_manual(interaction: discord.Interaction, member: discord.Member, mcname: str):
    service_channel = bot.get_channel(IDs.service_channel_id)
    answer = await db_requests.change_mcname(member.id, mcname)
    if answer:
        await interaction.response.send_message(f"The Minecraft name {mcname} was successfully updated!",ephemeral=True)
    else:
        await interaction.response.send_message("There is no valid Minecraft name!", ephemeral=True)

#region permission_error_handler
@add_user_manual.error
async def add_user_manual_error(interaction: discord.Interaction, error: app_commands.MissingPermissions):
    await interaction.response.send_message(f"{error}You have no permission for that command!", ephemeral=True)

@edit_name_manual.error
async def edit_name_manual_error(interaction: discord.Interaction, error: app_commands.MissingPermissions):
    await interaction.response.send_message("You have no permission for that command!", ephemeral=True)

@delete_user_manual.error
async def delete_user_manual_error(interaction: discord.Interaction, error: app_commands.MissingPermissions):
    await interaction.response.send_message(f"{error}You have no permission for that command!", ephemeral=True)
#endregion
#endregion

@tree.command(name="edit-mc-name",
              description="Edit or put in your exact minecraft name to register it. Leave a blank to delete your entry.")
async def editname(interaction: discord.Interaction, mcname: str):
    answer = await db_requests.change_mcname(interaction.user.id, mcname)
    if answer == True:
        await interaction.response.send_message(f"The Minecraft name {mcname} was successfully updated!", ephemeral=True)
    else:
        await interaction.response.send_message("There is no valid Minecraft name!",ephemeral=True)


@bot.event
async def on_member_join(member: discord.Member):
    welcome_channel = bot.get_channel(IDs.welcome_channel_id)
    await welcome_channel.send(
        f"Hallo und Herzlich wilkommen <@{member.id}>! Dies ist dein Ort, um dich mit den anderen Mitgliedern auszutauschen, Handel zu betreiben, usw. Bitte füge auch deinen MC Namen mit /edit-mc-name hinzu, damit andere sehen können, ob du online bist.")

    service_channel = bot.get_channel(IDs.service_channel_id)

    if await db_requests.new_member_entry(member.id):
        await service_channel.send(f"The User {member.name} was added successfully!")
    else:
        await service_channel.send(
            f"The User {member.name} already existed in the database! Please contact the support!")


# region userverlassen
@bot.event
async def on_member_remove(member: discord.Member):
    welcome_channel = bot.get_channel(IDs.welcome_channel_id)
    service_channel = bot.get_channel(IDs.service_channel_id)
    await welcome_channel.send(
        f"Unfortunately, the user {member.name} left us! We wish him all the best for the future!")
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
    await abfrage_online_player.start()


@tasks.loop(minutes=5)
async def abfrage_online_player():
    online_members = await mcrequests.request_member_status()
    if online_members:

        embed = await embeds.get_online_members_embed(online_members)

    else:

        embed = await embeds.get_no_online_members_embed()

    activity_channel = cast(discord.TextChannel, bot.get_channel(IDs.activity_channel_id))

    await activity_channel.purge(limit=None)

    await activity_channel.send(embed=embed)


token = os.getenv("TOKEN")
if token:
    bot.run(token)
