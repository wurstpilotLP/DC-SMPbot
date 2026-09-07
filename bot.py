# Needed Libraries
import discord
import sqlalchemy
from dotenv import load_dotenv
# Needed Variables

from discord import app_commands
from discord.ext import tasks


import IDs
import globals
# Needed methods
from mcrequests import request_member_status

# Everything about the Database

# Set up the Connection
connection = sqlalchemy.connect("playernames.db")

# Set up a cursor to read and edit the table
globals.cursor = connection.cursor()

# Create the Table (used only once with the first start of the Bot)
globals.cursor.execute("""CREATE TABLE IF NOT EXISTS list_mc_names (userid INTEGER, mcname TEXT)""")

# Intents

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


# Needed Methods

@tree.command(name="edit-mc-name", description="Edit or put in your exact minecraft name to register for the oline-status-page-levae a blanket to delete your entry")
async def editname(interaction=discord.Interaction,mc_name:str):
    if mcname=="":
        await interaction.response("Error: Please fill in your MC Name!")
        ephemeral=True
    else:
        user_id = interaction.user.id()
        cursor.execute("""INSERT OR REPLACE INTO list_mc_names(userid,mcname) VALUES(?,?)""",(user_id,mc_name))
        await interaction.response(f"Your MC name was successfully set to {mc_name}")
        ephemeral=True
    

@bot.event
async def on_member_join(member: discord.Member):
    member_id= member.id
    welcomechannel=bot.get_Channel(IDs.welcome_channel_id)
    await welcomechannel.send(f"Hallo und Herzlich wilkommen <@{member_id}>! Dies ist dein Ort, um dich mit den anderen Mitgliedern auszutauschen, Handel zu betreiben, usw. Bitte füge auch deinen MC Namen mit /edit-mc-name hinzu, damit andere sehen können, ob du online bist.")
    # edit the Text of the welcome-message in the format welcomechannel.send(f"place your text")
    # if you want to mention the user, just write <@{member_id}> directly into your text.

@bot.event
async def on_member_remove(member:discord.Member):
    welcomechannel=bot.get_Channel(IDs.welcome_channel_id)
    await welcomechannel.send(f"Der User {member.name} hat uns leider verlassen! Wir wünschen ihm weiter alles Gute!)
    # here, you can also edit the leave-message by typing welcomechannel.send(f"put your text here")
    # to put the name of the user who left into this message, just write {member.name} into the text
    
    cursor.execute("DELETE FROM list_mc_names WHERE userid=?", (member.id,))


@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot ist online als {bot.user.name}, die Commands sind synchronisiert!")
    globals.bot = bot

@tasks.loop(minutes=5)
async def abfrage_online_player():
    online_members = await request_member_status
    if online_members:
        
        embed=get_embed_(player_list_string)
    else:
        embed=get_embed_no_members()

    activity_channel=
        
    

bot.run(TOKEN)