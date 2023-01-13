from sqlalchemy import Column, Integer, String, ForeignKey

from src.db.db import Base


class StudentInfo(Base):
    __tablename__ = 'student_info'
    __table_args__ = {"comment": "Информация о студенте"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи Информация о студенте")
    description = Column(String, nullable=False, comment="описание")
    address = Column(String, nullable=False, comment="адрес")
    student_id = Column(Integer(), ForeignKey('student.id'))

    def __init__(self, student_id: int, description: str, address: str):
        self.student_id = student_id
        self.description = description
        self.address = address

    def __repr__(self):
        return f'#StudentInfo: {self.name}, id={self.id} \n'
