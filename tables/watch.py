from db.db import SessionLocal
from tables.generate_tables import Student, Faculty, Housing

session = SessionLocal()

for it in session.query(Student):
    ...
    # print(it)


# for i, it in enumerate(session.query(Faculty)):
#     # ...
#     print(i, it)
#     print(len(it.students))
#     print('-' * 10)

# for i, it in enumerate(session.query(Housing)):
#     # print(*it.faculty, end='\n\n\n')
#     for f in it.faculty:
#         print(f)
#     print('-' * 50)




