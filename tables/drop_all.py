from db.db import Base, engine

from models.faculty import Faculty
from models.group import Group
from models.housing import Housing
from models.subject import Subject
from models.group_subject import group_subject

Base.metadata.drop_all(bind=engine)
