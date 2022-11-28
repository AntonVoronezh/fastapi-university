from db.db import Base
from sqlalchemy import Column, Integer, String


class Group(Base):
    __tablename__ = 'group'
    __table_args__ = {"comment": "Группы"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи группы")
    name = Column(String(255), nullable=False, unique=True, comment="Название группы")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'#Group: {self.name}, id={self.id} \n'