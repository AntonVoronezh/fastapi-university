from db.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Faculty(Base):
    __tablename__ = 'faculty'
    __table_args__ = {"comment": "Факультеты"}

    id = Column(Integer, primary_key=True, comment="Идентификатор записи факультета")
    name = Column(String(255), nullable=False, unique=True, comment="Название факультета")
    groups = relationship("Group")
    housings = relationship("Housing")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'#Faculty: {self.name}, id={self.id}, groups={self.groups} \n'
