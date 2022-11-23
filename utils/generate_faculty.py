from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from faker import Faker


from db.db import SessionLocal, engine, Base
from utils.generate_tables import Faculty

fake = Faker('ru_RU')

housing_ = ['Alfa', 'Bravo', 'Charly', 'Ecco', 'Delta']
name_ = [
    'Факультет географии',
    'Факультет экологии ',
    'Факультет туризма',
    'Факультет журналистики',
    'Факультет Истории',
    'Факультет математики',
    'Факультет биологии',
    'Факультет физики',
    'Факультет философии',
]




db = SessionLocal()

name = fake.random_choices(elements=name_, length=1)[0]

for h in name_:
    ...
#     housing = fake.random_choices(elements=housing_, length=1)[0]
#     print(h, housing)
#
#     faculty = Faculty(name=h, housing=housing)
#
#     db.add(faculty)  # добавляем в бд
#     db.commit()  # сохраняем изменения
#
# db.close()
