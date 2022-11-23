from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from faker import Faker
import os

from random import random
from db.db import SessionLocal, engine, Base

import generate_faculty
from utils.generate_tables import Student

fake = Faker('ru_RU')



# active = random.choice(bools)
# weight = facker.random.randint(10, 100)
# priority = random.choice(list(TodoTypeEnum))


# print(fake.paragraph(nb_sentences=5))
# # print(facker.lexify(text='Random Identifier: ??????????'))
# # print(facker.bothify(text='Product Number: ????-########', letters='ABCDE'))
# # print(facker.numerify(text='Intel Core i%-%%##K vs AMD Ryzen % %%##X'))





db = SessionLocal()
#
name = fake.name()
address = fake.address()
age = fake.random.randint(18, 25)
course = fake.random.randint(1, 5)
group = fake.random.randint(1, 10)
faculty_id = fake.random.randint(1, 9)

student = Student(name=name, address=address, age=age, course=course, group=group, faculty_id=faculty_id)

db.add(student)     # добавляем в бд
db.commit()     # сохраняем изменения
db.close()


