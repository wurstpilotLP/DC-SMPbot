import discord

async def get_list_bulletpoints(values):
    return list_bulletpoints="/n".join(f"• {name}" for name in values)

async def get_list_bulletpoints_text():
    