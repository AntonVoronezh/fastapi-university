from db.db import Base
from sqlalchemy import Column, Integer, String

class Subject(Base):
    __tablename__ = 'subject'
    __table_args__ = {"comment": "Предметы"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи Предмета")
    name = Column(String(255), nullable=False, unique=True, comment="Название Предмета")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'#Subject: {self.name}, id={self.id} \n'
