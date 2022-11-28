from db.db import SessionLocal
from models.faculty import Faculty
from models.housing import Housing

session = SessionLocal()


def get_all_faculty():
    res = []
    for it in session.query(Faculty):
        if __name__ == "__main__":
            print(f'{it.id} - {it.name}')
        res.append(it)
    return res


def get_all_housing():
    res = []
    for it in session.query(Housing):
        if __name__ == "__main__":
            print(f'{it.id} - {it.name}')
        res.append(it)
    return res


# get_all_faculty()
get_all_housing()

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
