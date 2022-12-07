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
