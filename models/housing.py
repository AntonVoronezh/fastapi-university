from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Housing(Base):
    __tablename__ = 'housing'
    __table_args__ = {"comment": "Корпуса"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи корпуса")
    name = Column(String(255), nullable=False, unique=True, comment="Название корпуса")
    faculty_id = Column(Integer, ForeignKey('faculty.id'))

    def __init__(self, name: str, faculty_id: int):
        self.name = name
        self.faculty_id = faculty_id

    def __repr__(self):
        return f'#Housing: {self.name}, id={self.id} \n'
