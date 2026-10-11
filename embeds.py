from datetime import datetime, timezone

import discord

async def get_list_bulletpoints(values):
    return "\n".join(f"• {name}" for name in values)

#region mc_activity_feed
async def get_online_members_embed(online_members):
    embed = discord.Embed(
        title = "The following members are online",
        colour = discord.Colour.green(),
        description = await get_list_bulletpoints(online_members),
        timestamp = datetime.now(timezone.utc)
    )
    return embed

async def get_no_online_members_embed():
    embed = discord.Embed(
        title = "There are no online members",
        colour = discord.Colour.red(),
        description = "Be the first one!",
        timestamp = datetime.now(timezone.utc)
    )
    return embed
#endregion

#region database_edits

async def get_member_deleted_embed(deleted_member_name):
    embed = discord.Embed(
        title = "Success!",
        description = f"{deleted_member_name} was deleted",
        colour = discord.Colour.green(),
        timestamp = datetime.now(timezone.utc)
    )
    return embed

async def get_new_member_entry_embed(new_member_name):
    embed = discord.Embed(
        title = "Success!",
        description = f"{new_member_name} was added",
        colour = discord.Colour.green(),
        timestamp = datetime.now(timezone.utc)
    )
    return embed

async def get_member_deleted_error_embed(member_name):
    embed = discord.Embed(
        title = "Error",
        description = f"There was a problem with deleting {member_name}. Please contact support.",
        colour = discord.Colour.red(),
        timestamp = datetime.now(timezone.utc)
    )
    return embed

async def get_new_member_entry_error_embed(member_name):
    embed = discord.Embed(
        title = f"Error",
        description = f"There was a problem with adding {member_name}. Please contact support.",
        colour = discord.Colour.red(),
        timestamp = datetime.now(timezone.utc)
    )
    return embed

async def get_mcname_changed_embed(mc_name,member_name):
    embed = discord.Embed(
        title = "Success!",
        description = f"{member_name}'s Minecraft name was successfully changed to {mc_name}!",
        colour = discord.Colour.green(),
        timestamp = datetime.now(timezone.utc)
    )
    return embed

async def get_mcname_changed_error_embed(mc_name,member_name):
    embed = discord.Embed(
        title = "Error",
        description = f"There was a problem with changing {member_name}'s Minecraft name to {mc_name}. Please contact support.",
        colour = discord.Colour.red(),
        timestamp = datetime.now(timezone.utc)
    )
    return embed
#endregion

#region no_permission

async def get_error_embed(error):
    embed = discord.Embed(
        title = "Error",
        description = f"There was an error: {error}",
        colour = discord.Colour.red()
    )
    return embed

#endregion

#region join_leave

async def get_member_joined_embed(new_member):
    embed = discord.Embed(
        title = f"Welcome {new_member.mention}!",
        description = f"Welcome to our Discord Server! Feel free to look around! Also check out to see the activity feed to see who is currently playing on the server!\n\nIf you need help please contact support.",
        colour = discord.Colour.yellow()
    )
    return embed

async def get_member_left_embed(member):
    embed = discord.Embed(
        title = f"Goodbye {member.mention}!",
        description = "We wish him the best for the future and thank him for his Service!",
        colour = discord.Colour.brand_red()
    )
    return embed

#endregion