import discord

async def get_list_bulletpoints(values,):
    return "/n".join(f"• {name}" for name in values)

async def get_online_members_embed(online_members):
    embed = discord.Embed(
        title="The following members"
    )