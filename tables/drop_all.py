from db.db import Base, engine

from generate_tables import Student, Faculty

Base.metadata.drop_all(bind=engine)
