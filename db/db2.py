from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg2://root:root@localhost/test_db")
# engine.connect()
# print(engine)

# создаем модель, объекты которой будут храниться в бд
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)

# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# создаем объект Person для добавления в бд
tom = Person(name="Tom", age=38)
db.add(tom)     # добавляем в бд
db.commit()     # сохраняем изменения

print(tom.id)   # можно получить установленный id

# приложение, которое ничего не делает
# app = FastAPI()

