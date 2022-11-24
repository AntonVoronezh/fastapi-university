from db.db import SessionLocal
from tables.generate_tables import Student, Faculty

session = SessionLocal()

for it in session.query(Student):
    ...
    # print(it)


for i, it in enumerate(session.query(Faculty)):
    # ...
    print(i, it)
    print(len(it.students))
    print('-' * 10)




