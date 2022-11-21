from faker import Faker
import os

from random import random

from db.db import create_db, Session
from db.models import Student

# from models.student import Student

fake = Faker('ru_RU')

name = fake.name()
# description = fake.address()
# active = random.choice(bools)
# weight = facker.random.randint(10, 100)
# priority = random.choice(list(TodoTypeEnum))

# student = Student(name)
# create_db()
#
# db.add(student)
# db.commit()
# db.close()

# print(fake.paragraph(nb_sentences=5))
# # print(facker.lexify(text='Random Identifier: ??????????'))
# # print(facker.bothify(text='Product Number: ????-########', letters='ABCDE'))
# # print(facker.numerify(text='Intel Core i%-%%##K vs AMD Ryzen % %%##X'))


db_is_created = os.path.exists('test_db')
print(db_is_created)
create_db()
db_is_created = os.path.exists('test_db')
print(db_is_created)
# create_db()
#
# session = Session()
#
# student = Student(name)
#
# session.add(student)
#
# session.commit()
# session.close()
