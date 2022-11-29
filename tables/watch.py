from db.db import SessionLocal
from models.faculty import Faculty
from models.group import Group
from models.housing import Housing
from models.subject import Subject

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


def get_all_group():
    res = []
    for it in session.query(Group):
        if __name__ == "__main__":
            print(f'{it.id} - {it.name}')
        res.append(it)
    return res


def get_all_subject():
    res = []
    for it in session.query(Subject):
        if __name__ == "__main__":
            print(f'{it.id} - {it.name}')
        res.append(it)
    return res


get_all_faculty()
# get_all_housing()
# get_all_group()
# get_all_subject()

