
from sqlalchemy import or_, and_, not_, desc
from db.db import SessionLocal
from models.faculty import Faculty
from models.housing import Housing
from models.subject import Subject
from models.group import Group
from models.student import Student
from models.group import Group
from models.student_info import StudentInfo
from models.faculty_info import FacultyInfo

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


# get_all_faculty()
# get_all_housing()
# get_all_group()
# get_all_subject()



# SELECT * FROM public.faculty
def get_all():
    res = []
    for it in session.query(Faculty).all():
        if __name__ == "__main__":
            print(f'{it.id} - {it.name}')
        res.append(it)
    return res

# get_all()

# SELECT (faculty.id, faculty.name) FROM faculty
# SELECT faculty.id FROM faculty
def get_all_(): # [(1, 'aaaa')] возвращает кортедж
    res = []
    for it in session.query(Faculty.name, Faculty.id).all():
        res.append(it)
    return res

# print(get_all_())


# SELECT COUNT(*) FROM public.faculty
def get_count():
    res = session.query(Faculty).count()
    print(res)
    return res

# get_count()


#
def get_first(): # первый результат или None
    res = session.query(Faculty).first()
    return res

# print(get_first())


#  первую колонку первой записи или None, если результат пустой.
#  Если записей несколько, то бросает исключение MultipleResultsFound
def get_scalar():
    res = session.query(Faculty).scalar()
    # print(res)
    print(bool(res))
    # return res

# get_scalar()


#  Возвращает объект по первичному ключу или None, если объект не был найден
# SELECT * FROM faculty WHERE(id = 3)
def get_get():
    res = session.query(Faculty).get(3)
    print(res)


# get_get()


#  отфильтровать результаты
#
def get_filter():
    # SELECT * FROM faculty WHERE name = 'Факультет права' AND id = 14
    # res = session.query(Faculty).filter(Faculty.name == 'Факультет права', Faculty.id == 14)
    # res = session.query(Faculty).filter(and_(Faculty.name == 'Факультет права', Faculty.id == 14)).all()
    # SELECT * FROM faculty WHERE name = 'Факультет права' OR id = 14
    # res = session.query(Faculty).filter(or_(Faculty.name == 'Факультет права', Faculty.id == 13)).all()
    # SELECT * FROM faculty WHERE name = 'Факультет права' AND id != 13
    # res = session.query(Faculty).filter(and_(Faculty.name == 'Факультет права', not_(Faculty.id == 13))).all()
    # SELECT * FROM faculty WHERE name IS NULL
    # res = session.query(Faculty).filter(Faculty.name == None)
    # SELECT * FROM faculty WHERE name IS NOT NULL
    # res = session.query(Faculty).filter(Faculty.name != None).all()
    # SELECT * FROM faculty WHERE name IN ('Факультет права')
    # res = session.query(Faculty).filter(Faculty.name.in_(['Факультет права']))
    # SELECT * FROM faculty WHERE name NOT IN ('Факультет права')
    # res = session.query(Faculty).filter(Faculty.name.notin_(['Факультет права'])).all()
    # SELECT * FROM faculty WHERE id BETWEEN 1 AND 4
    # res = session.query(Faculty).filter(Faculty.id.between(1,3))
    # SELECT * FROM faculty WHERE id BETWEEN 1 AND 4
    # res = session.query(Faculty).filter(Faculty.id.between(1,3))
    # SELECT * FROM faculty WHERE id NOT BETWEEN 1 AND 4
    # res = session.query(Faculty).filter(not_(Faculty.id.between(1,3)))
    # SELECT * FROM faculty WHERE name LIKE 'ф%'
    # res = session.query(Faculty).filter(Faculty.name.like("%ф"))
    # SELECT * FROM faculty WHERE name ILIKE 'ф%'
    # res = session.query(Faculty).filter(Faculty.name.ilike("ф%")).all()
    # SELECT * FROM faculty WHERE name NOT LIKE 'ф%'
    res = session.query(Faculty).filter(not_(Faculty.name.ilike("ф%"))).all()


    print(res)


# get_filter()


def get_limit():
    # SELECT * FROM faculty LIMIT 3
    # res = session.query(Faculty).limit(3)
    res = session.query(Faculty).offset(3).all()
    print(res)


# get_limit()


# для сортировки, по умолчанию asc
def get_order_by():
    # SELECT * FROM faculty ORDER BY name
    # res = session.query(Faculty).order_by(Faculty.name)
    # SELECT * FROM faculty ORDER BY name DESC
    res = session.query(Faculty).order_by(desc(Faculty.name))
    print(res)


# get_order_by()


# используется для объединения строк из двух или более таблиц на основе общего поля между ними
# ля получения данных из одной или нескольких таблиц в одном запросе
# SQL INNER JOIN
def get_inner_join():
    # SELECT * FROM faculty JOIN faculty_info ON faculty.id = faculty_info.faculty_id
    # res = session.query(Faculty).join(FacultyInfo).all()

# польностью несколько таблиц сразу
    # SELECT * FROM faculty
    # JOIN faculty_info ON faculty.id = faculty_info.faculty_id
    # JOIN housing ON faculty.id = housing.faculty_id
    # res = session.query(Faculty).join(FacultyInfo).join(Housing)


# некторые данные из нескольких таблиц сразу
    # SELECT (faculty.name, "group".name )
    # FROM faculty JOIN "group" ON faculty.id = "group".faculty_id
    res = session.query(Faculty.name, Group.name).join(Group)
    print(res)


# get_inner_join()



# используется для объединения строк из двух или более таблиц на основе общего поля между ними
# ля получения данных из одной или нескольких таблиц в одном запросе
# LEFT OUTER JOIN
def get_outer_join():
    # SELECT (faculty.name, "group".name )
    # FROM faculty JOIN "group" ON faculty.id = "group".faculty_id
    # res = session.query(Student.first_name, Group.name).join(Group).all()
    res = session.query(Student.first_name, Group.name).outerjoin(Group).all()
    print(res)

get_outer_join()
