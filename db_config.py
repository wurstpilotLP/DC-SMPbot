import sqlalchemy as db_lib
from sqlalchemy.ext.asyncio import create_async_engine
import sqlalchemy.orm as db_orm

Base = db_orm.declarative_base()

# My table for the mcnames
class Member(Base):
    __tablename__ = "list_mcnames"

    userid: db_orm.Mapped[int] = db_orm.mapped_column(db_lib.Integer, primary_key=True)
    mcname: db_orm.Mapped[str] = db_orm.mapped_column(nullable=True)

database_url="sqlite+aiosqlite:///./database.sqlite"

engine = db_lib.ext.asyncio.create_async_engine(database_url)

SessionLocal = db_lib.ext.asyncio.async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)