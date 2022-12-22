from db.db import Base, engine

from models.student import Student

Base.metadata.drop_all(bind=engine)
