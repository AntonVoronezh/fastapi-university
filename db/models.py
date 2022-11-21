from sqlalchemy import Column, Integer, String

from db import db


class Student(db.Base):
    __tablename__ = 'students'
    __table_args__ = {"comment": "Студенты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи студента")
    name = Column(String(255), nullable=False, unique=True, comment="Имя студента")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        print(f'[Name: {self.name}]')
