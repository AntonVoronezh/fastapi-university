from functools import lru_cache
from typing import Generator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker

from src.db.config import get_settings

engine = create_engine(get_settings().database_url, pool_pre_ping=True)


@lru_cache
def create_session() -> scoped_session:
    Session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return Session


def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()
    try:
        yield Session
    finally:
        Session.remove()


# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker

# DATABASE_URL = "postgresql+psycopg2://root:root@localhost/test_db"

# engine = create_engine(get_settings().database_url, pool_size=20, max_overflow=0)
# engine.connect()
# print(engine)


# создаем модель, объекты которой будут храниться в бд
Base = declarative_base()

engine = create_async_engine(
    get_settings().database_url, echo=True
)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_db():
    async with async_session() as session:
        try:  # noqa: WPS501
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_user_db(session: AsyncSession = Depends(get_async_db)):
    yield SQLAlchemyUserDatabase(session, User)
