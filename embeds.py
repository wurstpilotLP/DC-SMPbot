from datetime import datetime, timezone

import discord

async def get_list_bulletpoints(values):
    return "/n".join(f"• {name}" for name in values)

#region mc_activity_feed
async def get_online_members_embed(online_members):
    embed = discord.Embed(
        title="The following members are online",
        colour=discord.Colour.green(),
        description = await get_list_bulletpoints(online_members),
        timestamp = datetime.now(timezone.utc)
    )
    return embed

async def get_no_online_members_embed():
    embed = discord.Embed(
        title="There are no online members",
        colour=discord.Colour.red(),
        description = "Be the first one!",
        timestamp = datetime.now(timezone.utc)
    )
    return embed
#endregion