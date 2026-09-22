# Needed Libraries
import discord
import dotenv

# Needed Variables

import IDs
import globals
from globals import bot

# Needed methods
from db_config import init_db
import db_requests

# Intents

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)


# Needed Methods

@tree.command(name="edit-mc-name",
              description="Edit or put in your exact minecraft name to register for the oline-status-page-levae a blanket to delete your entry")
async def editname(interaction=discord.Interaction, mcname: str):
    pass


@bot.event
async def on_member_join(member: discord.Member):
    welcome_channel = bot.get_Channel(IDs.welcome_channel_id)
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
        await service_channel.send(f"The User {member.name} never existed in the database! please contact the support!")
# endregion

@bot.event
async def on_ready():
    await init_db()
    await tree.sync()
    print(f"Bot ist online als {bot.user.name}, die Commands sind synchronisiert!")
    globals.bot = bot

@tasks.loop(minutes=5)
async def abfrage_online_player():
    online_members = await request_member_status
    if online_members:

        embed = get_embed_(player_list_string)
    else:
        embed = get_embed_no_members()

    activity_channel =

bot.run(TOKEN)
