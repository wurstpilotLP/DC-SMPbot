import sqlite
from globals import cursor

async def get_known_players():
    cursor.execute("SELECT mcname FROM userid")
    all_players=cursor.fetchall()
    return [line[0] for line in all_players]