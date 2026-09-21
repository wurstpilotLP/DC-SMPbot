import sqlalchemy as db_lib

class Base (db_lib.DeclarativeBase):
    pass
# My table for the mcnames
class Member(Base):
    __tablename__ = "list_mcnames"

    userid: db_lib.Mapped[int] = db_lib.orm.Column(db_lib.Integer, primary_key=True)
    mcname: db_lib.Mapped[str] = db_lib.orm.Column(db_lib.Integer, Nullable=True)

database_url="sqlite:///./database.sqlite"

engine = db_lib.ext.asyncio.create_aysnc_engine(database_url)

SessionLocal = db_lib.ext.asyncio.async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)