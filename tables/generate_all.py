from faker import Faker
from random import randint

from db.db import SessionLocal
from models.faculty_info import FacultyInfo
from models.student import Student
from models.student_info import StudentInfo
from models.subject import Subject
from tables.generate_tables import Faculty, Housing, Group
from tables.watch import get_all_faculty, get_all_housing, get_all_group, get_all_subject

fake = Faker('ru_RU')
db = SessionLocal()


def gen_arr(in_list):
    ran = randint(3, 6)
    use = []
    # print(ran)
    # print('#' * 10)
    for r in range(ran):
        ra = randint(0, len(in_list) - 1)

        if ra not in use:
            use.append(ra)
    # print(use)
    return use


housing_names = [
    'Alfa', 'Bravo', 'Charly', 'Ecco', 'Delta', 'Foxtrot',
    'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima']
faculty_names = [
    'Факультет географии', 'Факультет экологии', 'Факультет туризма', 'Факультет журналистики',
    'Факультет истории', 'Факультет математики', 'Факультет биологии', 'Факультет физики',
    'Факультет философии', 'Факультет химии', 'Факультет медицины', 'Факультет фармацевтики',
    'Факультет психологии', 'Факультет права', 'Факультет юриспруденции', 'Факультет экономики',
    'Факультет геологии', 'Факультет отношений'
]
academic_subject = [
    'Авто', 'Мото', 'Бизнес','Финансы', 'Города', 'Страны', 'Гороскопы', 'Магия', 'Гадания',
    'Досуг', 'Развлечения', 'Еда', 'Кулинария', 'Животные', 'Растения', 'Знакомства', 'Любовь',
    'Искусство', 'Культура', 'Видео игры', 'Компьютеры', 'Связь', 'Красота', 'Здоровье',
    'Наука', 'Техника', 'Языки', 'Общество', 'Политика', 'СМИ', 'Программирование',
    'Путешествия', 'Туризм', 'Работа', 'Карьера', 'Семья', 'Дом', 'Дети', 'Отношения',
]
group_names = []
group_by_course_names = []

for name in faculty_names:
    spl = name.split(' ')
    name_f = f'{spl[0][0:1].upper()}-{spl[1][0:4].upper()}'
    group_names.append(name_f)

for i in range(5):
    group_by_course_names.append([])
    for j in group_names:
        group_by_course_names[i].append(f'{j}:{i+1}')



# факультеты
for item in faculty_names:
    faculty = Faculty(name=item)
    db.add(faculty)
db.commit()
db.close()

# print(*get_all_faculty(), sep='')

# корпуса
for item in housing_names:
    housing = Housing(name=item, faculty_id=None)
    arr = gen_arr(get_all_faculty())

    db.add(housing)
db.commit()
db.close()

# print(*get_all_housing(), sep='')


# группы
for item in group_by_course_names:
    for it in item:
        course = int(it.split(':')[1])

        group = Group(name=it, course=course, faculty_id=None, housing_id=None)

        db.add(group)
db.commit()
db.close()

# print(*get_all_group(), sep='')


# предметы
for sub in academic_subject:
    subject = Subject(name=sub)

    db.add(subject)
db.commit()
db.close()

# print(*get_all_subject(), sep='')


# в группы добавить факультеты (один ко многим)
for item in db.query(Group):
    faculty_id = None
    for f in db.query(Faculty):
        spl_f = f.name.split(' ')
        spl_name = item.name.split(':')
        if f'{spl_f[0][0:1].upper()}-{spl_f[1][0:4].upper()}' == spl_name[0]:
            faculty_id = f.id

    item.faculty_id = faculty_id
    db.add(item)
db.commit()
db.close()

# print(*get_all_group(), sep='')


# в корпуса добавить факультеты (один ко многим)
for item in db.query(Housing):
    f = []
    for it in db.query(Faculty):
        f.append(it)
    rand = randint(0, len(f) - 1)
    faculty_id = f[rand].id
    item.faculty_id = faculty_id

    db.add(item)
db.commit()
db.close()

# print(*get_all_housing(), sep='')


# в корпуса добавить группы (один ко многим)
for item in db.query(Group):
    f = []
    for it in db.query(Housing):
        f.append(it)
    rand = randint(0, len(f) - 1)
    housing_id = f[rand].id
    item.housing_id = housing_id

    db.add(item)
db.commit()
db.close()
# print(*get_all_group(), sep='')


# в группы добавить предметы (многие ко многим)
for item in db.query(Subject):
    f = []
    for it in db.query(Group):
        f.append(it)
    for i in range(25):
        rand = randint(0, len(f) - 1)
        item.groups.append(f[rand])

    db.add(item)
db.commit()
db.close()


# в факультеты добавить описание (один к одному)
for item in db.query(Faculty):
    description = fake.paragraphs(nb=5)
    img = fake.file_extension(category='image')
    item.info = FacultyInfo(description=description, img=img, faculty_id=item.id)
    db.add(item)
db.commit()
db.close()



# добавить студентов
for item in range(100):
    f = fake.name().split(' ')
    first_name = f[0]
    second_name = f[1]
    family = f[2]
    age = randint(18, 30)
    student = Student(first_name=first_name, second_name=second_name, family=family, age=age, group_id=None)

    db.add(student)
db.commit()
db.close()


# в студентов добавить описание (один к одному)
for item in db.query(Student):
    description = fake.paragraphs(nb=4)
    img = fake.file_extension(category='image')
    address = fake.address()
    item.info = StudentInfo(description=description, img=img, student_id=item.id, address=address)
    db.add(item)
db.commit()
db.close()

# в группы добавить студентов (один ко многим)
for item in db.query(Student):
    f = []
    for it in db.query(Group):
        f.append(it)
    rand = randint(0, len(f) - 1)
    item.group_id = f[rand].id

    db.add(item)
db.commit()
db.close()



