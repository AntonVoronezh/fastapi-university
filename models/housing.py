from db.db import Base
from sqlalchemy import Column, Integer, String

class Housing(Base):
    __tablename__ = 'housing'
    __table_args__ = {"comment": "Корпуса"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи корпуса")
    name = Column(String(255), nullable=False, unique=True, comment="Название корпуса")
    # faculty = relationship("Faculty", secondary=faculty_housing, backref="housing")
    # group = relationship('Group', backref='group', uselist=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'#Housing: {self.name}, id={self.id} \n'
