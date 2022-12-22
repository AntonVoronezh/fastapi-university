from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from db.config import get_settings

engine = create_engine("postgresql+psycopg2://root:root@localhost/test_db", pool_pre_ping=True)


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



from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+psycopg2://root:root@localhost/test_db"

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
# engine.connect()
# print(engine)


# создаем модель, объекты которой будут храниться в бд
Base = declarative_base()


# создаем таблицы
# Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)

db = SessionLocal()
