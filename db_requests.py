import sqlite
from globals import cursor
import sqlalchemy.orm as db_lib


class Base (db_lib.DeclarativeBase):
    pass

class Member(Base):
    __tablename__ = "list_mc_names"

    userid: db_lib.Mapped[int] = db_lib.Column(db_lib.Integer, primary_key=True)
    mcname: db_lib.Mapped[str] = db_lib.Column(db_lib.Integer, Nullable=True)

async def new_member_entry(userid):
    pass

async def change_mcname(userid, mcname):
    pass

async def get_mcname(userid):
    pass

async def get_known_players():
    cursor.execute("SELECT mcname FROM userid")
    all_players=cursor.fetchall()
    return [line[0] for line in all_players]