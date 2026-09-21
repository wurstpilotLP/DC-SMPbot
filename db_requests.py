import sqlalchemy as db_lib
import db_config as db
from db_config import Base


async def new_member_entry(userid):
    async with db.SessionLocal() as session:

        new_entry = db.Base(userid=userid)
        await session.add(new_entry)

        await session.commit()

async def change_mcname(userid, mcname):
    async with db.SessionLocal() as session:
        search_statement = db_lib.select(db.Member).where(db.Member.userid == userid)

        searched_user = await session.execute(search_statement)

        if searched_user == None:
            return


async def get_mcname(userid):
    async with db.SessionLocal() as session:
        search_statement = db_lib.select(db.Member).where(db.Member.userid == userid)

        result = await session.execute(search_statement)

        searched_user = result.scalar_one_or_none()

        if searched_user is not None:
            if searched_user.mcname != None:
                return searched_user.mcname
            else:
                return ""
        else:
            return None


async def get_known_players():
    pass