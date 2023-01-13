import contextlib
import asyncio
from random import randint

from faker import Faker
from fastapi import Depends
from fastapi_users.exceptions import UserAlreadyExists
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db.config import get_settings
from src.db.db import get_user_db, get_async_db
from src.models import StudentInfo
from src.models.student import Student
from src.modules.user.dto import UserCreate
from src.modules.user.service import UserManager

fake = Faker('ru_RU')

# DATABASE_URL = "postgresql+psycopg2://root:root@localhost/test_db"
engine = create_engine(get_settings().database_url_q, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# добавить студентов
for item in range(100):
    f = fake.name().split(' ')
    first_name = f[0]
    second_name = f[1]
    family = f[2]
    age = randint(18, 30)
    student = Student(first_name=first_name, second_name=second_name, family=family, age=age)

    db.add(student)
db.commit()
db.close()

# в студентов добавить описание (один к одному)
for item in db.query(Student):
    print(item.id)
    description = fake.paragraphs(nb=4)
    address = fake.address()
    item.info = StudentInfo(description=description, student_id=item.id, address=address)
    db.add(item)
db.commit()
db.close()


# создание юзера
async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


get_async_session_context = contextlib.asynccontextmanager(get_async_db)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(email: str, password: str, is_superuser: bool = False):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            email=email, password=password, is_superuser=is_superuser
                        )
                    )
                    print(f"User created {user}")
    except UserAlreadyExists:
        print(f"User {email} already exists")


asyncio.run(create_user('2@2.ru', '2', True))
