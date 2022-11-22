from sqlalchemy import Column, Integer, String
from faker import Faker

from db.db import SessionLocal, engine, Base

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


class Faculty(Base):
    __tablename__ = 'faculty'
    __table_args__ = {"comment": "Факультеты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи факультета")
    name = Column(String(255), nullable=False, unique=True, comment="Название факультета")
    housing = Column(String(255), nullable=False, comment="Корпус факультета")

    def __init__(self, name: str, housing: str):
        self.name = name
        self.housing = housing

    def __repr__(self):
        print(f'[Name: {self.name}]')


Base.metadata.create_all(bind=engine)

db = SessionLocal()

name = fake.random_choices(elements=name_, length=1)[0]

for h in name_:
    ...
    # housing = fake.random_choices(elements=housing_, length=1)[0]
    # print(h, housing)
    #
    # faculty = Faculty(name=h, housing=housing)
    #
    # db.add(faculty)  # добавляем в бд
    # db.commit()  # сохраняем изменения

# db.close()
