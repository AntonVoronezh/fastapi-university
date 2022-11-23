from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.db import Base, engine


class Student(Base):
    __tablename__ = 'student'
    __table_args__ = {"comment": "Студенты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи студента")
    name = Column(String(255), nullable=False, unique=True, comment="Имя студента")
    address = Column(String(255), nullable=False, unique=True, comment="Адрес студента")
    age = Column(Integer, nullable=False, comment="Возраст студента")
    course = Column(Integer, nullable=False, comment="Курс студента")
    group = Column(Integer, nullable=False, comment="Группа студента")
    faculty_id = Column(Integer, ForeignKey('faculty.id'))

    def __init__(self, name: str, address: str, age: int, course: int, group: int, faculty_id: int):
        self.name = name
        self.address = address
        self.age = age
        self.course = course
        self.group = group
        self.faculty_id = faculty_id

    def __repr__(self):
        return f'#Student Name: {self.name.split(" ")[0]}, id={self.id}'


class Faculty(Base):
    __tablename__ = 'faculty'
    __table_args__ = {"comment": "Факультеты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи факультета")
    name = Column(String(255), nullable=False, unique=True, comment="Название факультета")
    housing = Column(String(255), nullable=False, comment="Корпус факультета")
    students = relationship("Student")

    def __init__(self, name: str, housing: str):
        self.name = name
        self.housing = housing

    def __repr__(self):
        return f'#Faculty: {self.name}, id={self.id}, housing={self.housing}, students={self.students} \n'


Base.metadata.create_all(bind=engine)
