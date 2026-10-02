import sqlalchemy as db_lib
import db_config as db

async def get_user(userid):
    async with db.SessionLocal() as session:
        search_statement = db_lib.select(db.Member).where(db.Member.userid == userid)
        result = await session.execute(search_statement)
        searched_user = result.scalar_one_or_none()
        if searched_user is not None:
            return searched_user
        else:
            return None

async def new_member_entry(userid):
    if await get_user(userid) is None:

        async with db.SessionLocal() as session:

            new_entry = db.Member(userid=userid)

            session.add(new_entry)

            await session.commit()

            if new_entry:
                return True
            else:
                return False
    else:
        return False

async def change_mcname(userid, mcname):
    if mcname == "":
        return False
    else:
        async with (db.SessionLocal() as session):
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

        searched_user = await get_user(userid)

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

        search_statement = db_lib.select(db.Member.mcname).where(db.Member.mcname.is_not(None))

        unpacked_names = await session.scalars(search_statement)

        list_mcnames = list(unpacked_names.all())

        if list_mcnames:

            return list_mcnames
        else:

            return None