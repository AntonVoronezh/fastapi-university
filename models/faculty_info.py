from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class FacultyInfo(Base):
    __tablename__ = 'faculty_info'
    __table_args__ = {"comment": "Информация о факультете"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи Информация о факультета")
    description = Column(String, nullable=False, comment="описание")
    img = Column(String, nullable=False, comment="картинка")
    faculty_id = Column(Integer(), ForeignKey('faculty.id'))

    def __init__(self, faculty_id: int or None, description: str or None, img: str or None, ):
        self.faculty_id = faculty_id
        self.description = description
        self.img = img

    def __repr__(self):
        return f'#FacultyInfo: {self.name}, id={self.id} \n'
