from sqlalchemy import Column, Integer, String
from faker import Faker
import os

from random import random
from db.db import SessionLocal, engine, Base

fake = Faker('ru_RU')


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = {"comment": "Студенты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи студента")
    name = Column(String(255), nullable=False, unique=True, comment="Имя студента")
    address = Column(String(255), nullable=False, unique=True, comment="Адрес студента")
    age = Column(Integer, nullable=False, comment="Возраст студента")
    course = Column(Integer, nullable=False, comment="Курс студента")
    group = Column(Integer, nullable=False, comment="Группа студента")

    def __init__(self, name: str, address: str, age: int, course: int, group: int):
        self.name = name
        self.address = address
        self.age = age
        self.course = course
        self.group = group


    def __repr__(self):
        print(f'[Name: {self.name}]')


# active = random.choice(bools)
# weight = facker.random.randint(10, 100)
# priority = random.choice(list(TodoTypeEnum))


# print(fake.paragraph(nb_sentences=5))
# # print(facker.lexify(text='Random Identifier: ??????????'))
# # print(facker.bothify(text='Product Number: ????-########', letters='ABCDE'))
# # print(facker.numerify(text='Intel Core i%-%%##K vs AMD Ryzen % %%##X'))




Base.metadata.create_all(bind=engine)

db = SessionLocal()
#
name = fake.name()
address = fake.address()
age = fake.random.randint(18, 25)
course = fake.random.randint(1, 5)
group = fake.random.randint(1, 10)
# faculty = fake.

student = Student(name=name, address=address, age=age, course=course, group=group)
#
db.add(student)     # добавляем в бд
db.commit()     # сохраняем изменения
db.close()


