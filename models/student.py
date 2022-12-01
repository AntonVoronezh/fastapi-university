from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = 'student'
    __table_args__ = {"comment": "Студенты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи Студента")
    first_name = Column(String(255), nullable=False, comment="Имя Студента")
    second_name = Column(String(255), nullable=False, comment="Отчество Студента")
    family = Column(String(255), nullable=False, comment="Фамилия Студента")
    age = Column(Integer, nullable=False, comment="Возраст Студента")
    info = relationship('StudentInfo', backref='student', uselist=False)
    group_id = Column(Integer, ForeignKey('group.id'))

    def __init__(self, first_name: str, second_name: str, family: str, age: int, group_id: int or None):
        self.first_name = first_name
        self.second_name = second_name
        self.family = family
        self.age = age
        self.group_id = group_id

    def __repr__(self):
        return f'#Student: {self.family}, id={self.id} \n'
