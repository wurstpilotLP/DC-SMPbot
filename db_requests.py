import sqlalchemy as db_lib
import db_config as db


async def new_member_entry(userid):
    async with db.SessionLocal() as session:

        new_entry = db.Base(userid=userid)
        await session.add(new_entry)

        await session.commit()

async def change_mcname(userid, mcname):
    if mcname == "":
        return False
    else:
        async with db.SessionLocal() as session:
            search_statement = db_lib.select(db.Member).where(db.Member.userid == userid)

            result = await session.execute(search_statement)

            searched_user = result.scalar_one_or_none()

            if searched_user is not None:
                searched_user.mcname = mcname
                await session.commit()
                return True
            else:
                return False

async def get_mcname(userid):
    async with db.SessionLocal() as session:
        search_statement = db_lib.select(db.Member).where(db.Member.userid == userid)

        result = await session.execute(search_statement)

        searched_user = result.scalar_one_or_none()

        if searched_user is not None:
            if searched_user.mcname is not None:
                return searched_user.mcname
            else:
                return ""
        else:
            return None

async def delete_member(userid):
    async with db.SessionLocal() as session:

        search_statement = db_lib.select(db.Member).where(db.Member.userid == userid)
        result = await session.execute(search_statement)
        searched_user = result.scalar_one_or_none()

        if searched_user is not None:
            await session.delete(searched_user)
            await session.commit()
            return True
        else:
            return False

async def get_known_players():
    async with db.SessionLocal() as session:

        search_statement = db_lib.select(db.Member.mcname).where(db.Member.mcname is not None)
        result = await session.execute(search_statement)
        unpacked_names = result.scalars()
        list_mcnames = list(unpacked_names.all())
        if list_mcnames:
            return list_mcnames
        else:
            return None