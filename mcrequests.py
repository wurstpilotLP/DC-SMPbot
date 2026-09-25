import aiohttp
from db_requests import get_known_players

from db_requests import get_known_players

link="https://map.worldera.net/maps/world/live/players.json"

async def get_player_data():
    async with aiohttp.ClientSession() as session:       #open the "browser"
        async with session.get(link) as response:      #get the "website" if possible
            return await response.json()                     #return the raw json data

async def get_player_list():
    raw_data = await get_player_data()                                       #get every information about every player available
    return [player["name"] for player in raw_data["players"]]                #filter out just the names and save them in a list

async def request_member_status():
    known_players = await get_known_players()
    if known_players is not None:

        online_player = await get_player_list()  # get the online players from the methods below
        online_members = []  # make a new list where every players name who is registered in the bot and oline is saved

        for player in known_players:  # go through all saved names
            if player in online_player:  # look if the player is online
                online_members.append(player)  # if the player is online, save its name in the list online_members
        return online_members       #return the list with the members registered in the bots database and online
    else:
        return None