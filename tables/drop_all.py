from db.db import Base, engine

from generate_tables import Student, Faculty, Faculty, Housing, faculty_housing

Base.metadata.drop_all(bind=engine)
