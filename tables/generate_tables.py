from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from db.db import Base, engine


class Student(Base):
    __tablename__ = 'student'
    __table_args__ = {"comment": "Студенты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи студента")
    first_name = Column(String(255), nullable=False, comment="Имя студента")
    second_name = Column(String(255), nullable=False, comment="Отчетсво студента")
    family = Column(String(255), nullable=False, comment="Фамилия студента")
    course = Column(Integer, nullable=False, comment="Курс студента")
    group = Column(Integer, nullable=False, comment="Группа студента")
    faculty_id = Column(Integer, ForeignKey('faculty.id', ondelete="CASCADE"))
    info = relationship('StudentInfo', backref='student', uselist=False)

    def __init__(self, first_name: str, second_name: str, family: str, course: int, group: int, faculty_id: int):
        self.first_name = first_name
        self.second_name = second_name
        self.family = family
        self.course = course
        self.group = group
        self.faculty_id = faculty_id

    def __repr__(self):
        return f'#Student Name: {self.family}, id={self.id}'


class StudentInfo(Base):
    __tablename__ = 'student_info'
    __table_args__ = {"comment": "Информаци о студенте"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи информаци о студенте")
    age = Column(String(255), comment="Название факультета")
    address = Column(String(255), unique=True, comment="Адрес студента")
    student_id = Column(Integer(), ForeignKey('student.id', ondelete="CASCADE"))

    def __init__(self, address: str or None, age: int or None, student_id: int):
        self.age = age
        self.address = address
        self.student_id = student_id

    def __repr__(self):
        return f'#StudentInfo: id={self.id} \n'


# через таблицу
faculty_housing = Table('faculty_housing', Base.metadata,
                        Column('faculty_id', Integer(), ForeignKey("faculty.id")),
                        Column('housing_id', Integer(), ForeignKey("housing.id"))
                        )


class Faculty(Base):
    __tablename__ = 'faculty'
    __table_args__ = {"comment": "Факультеты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи факультета")
    name = Column(String(255), nullable=False, unique=True, comment="Название факультета")
    students = relationship("Student")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'#Faculty: {self.name}, id={self.id}, students={self.students} \n'


class Housing(Base):
    __tablename__ = 'housing'
    __table_args__ = {"comment": "Корпуса"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи корпуса")
    name = Column(String(255), nullable=False, unique=True, comment="Название корпуса")
    faculty = relationship("Faculty", secondary=faculty_housing, backref="housing")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'#Housing: {self.name}, id={self.id} \n'


Base.metadata.create_all(bind=engine)
