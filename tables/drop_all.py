from db.db import Base, engine

from models.faculty import Faculty
from models.group import Group
from models.housing import Housing

Base.metadata.drop_all(bind=engine)
