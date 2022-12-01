from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class StudentInfo(Base):
    __tablename__ = 'student_info'
    __table_args__ = {"comment": "Информация о студенте"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи Информация о студенте")
    description = Column(String, nullable=False, comment="описание")
    address = Column(String, nullable=False, comment="адрес")
    img = Column(String, nullable=False, comment="картинка")
    student_id = Column(Integer(), ForeignKey('student.id'))

    def __init__(self, student_id: int or None, description: str or None, img: str or None, address: str or None ):
        self.student_id = student_id
        self.description = description
        self.img = img
        self.address = address

    def __repr__(self):
        return f'#FacultyInfo: {self.name}, id={self.id} \n'
