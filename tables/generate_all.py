from random import randint

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.student import Student

fake = Faker('ru_RU')

DATABASE_URL = "postgresql+psycopg2://root:root@localhost/test_db"
engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
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
