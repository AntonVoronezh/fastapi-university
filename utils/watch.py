from db.db import SessionLocal
from utils.generate_tables import Student, Faculty

session = SessionLocal()

for it in session.query(Student):
    ...
    # print(it)


for it in session.query(Faculty):
    # ...
    print(it)



