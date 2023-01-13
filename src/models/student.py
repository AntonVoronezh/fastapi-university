from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.db import Base


class Student(Base):
    __tablename__ = 'student'
    __table_args__ = {"comment": "Студенты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи Студента")
    first_name = Column(String(255), nullable=False, comment="Имя Студента")
    second_name = Column(String(255), nullable=False, comment="Отчество Студента")
    family = Column(String(255), nullable=False, comment="Фамилия Студента")
    age = Column(Integer, nullable=False, comment="Возраст Студента")
    info = relationship('StudentInfo', backref='student', uselist=False)

    def __init__(self, first_name: str, second_name: str, family: str, age: int):
        self.first_name = first_name
        self.second_name = second_name
        self.family = family
        self.age = age

    def __repr__(self):
        return f'#Student: {self.family} \n'
