# Needed Libraries
import discord
import dotenv

# Needed Variables

import IDs
import globals

# Needed methods
from db_config import init_db

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
    if mcname != "":
        user_id = interaction.user.id()
        cursor.execute("""INSERT OR REPLACE INTO list_mc_names(userid,mcname) VALUES(?,?)""", (user_id, mcname))
        await interaction.response(f"Your MC name was successfully set to {mcname}")
        ephemeral = True
    else:
        await interaction.response("Error: Please fill in your MC Name!")
        ephemeral = True


@bot.event
async def on_member_join(member: discord.Member):
    member_id = member.id
    welcomechannel = bot.get_Channel(IDs.welcome_channel_id)
    await welcomechannel.send(
        f"Hallo und Herzlich wilkommen <@{member_id}>! Dies ist dein Ort, um dich mit den anderen Mitgliedern auszutauschen, Handel zu betreiben, usw. Bitte füge auch deinen MC Namen mit /edit-mc-name hinzu, damit andere sehen können, ob du online bist.")
    # edit the Text of the welcome-message in the format welcomechannel.send(f"place your text")
    # if you want to mention the user, just write <@{member_id}> directly into your text.

# region userverlassen
@bot.event
async def on_member_remove(member: discord.Member):
    welcomechannel = bot.get_Channel(IDs.welcome_channel_id)
    await welcomechannel.send(f"Der User {member.name} hat uns leider verlassen! Wir wünschen ihm weiter alles Gute!")
    # here, you can also edit the leave-message by typing welcomechannel.send(f"put your text here")
    # to put the name of the user who left into this message, just write {member.name} into the text

    cursor.execute("DELETE FROM list_mc_names WHERE userid=?", (member.id,))
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
