from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Group(Base):
    __tablename__ = 'group'
    __table_args__ = {"comment": "Группы"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи группы")
    name = Column(String(255), nullable=False, unique=True, comment="Название группы")
    course = Column(Integer, nullable=False, comment="Курс группы")
    faculty_id = Column(Integer, ForeignKey('faculty.id'))
    housing_id = Column(Integer, ForeignKey('housing.id'))

    def __init__(self, name: str, course: int, faculty_id: int or None, housing_id: int or None):
        self.name = name
        self.course = course
        self.faculty_id = faculty_id
        self.housing_id = housing_id

    def __repr__(self):
        return f'#Group: {self.name}, id={self.id}, faculty_id={self.faculty_id} \n'
