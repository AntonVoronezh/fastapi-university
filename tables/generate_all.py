from faker import Faker
from random import randint

from db.db import SessionLocal
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
        group_by_course_names[i].append(f'{j}:{i}')


faculty_list = []
housing_list = []
group_list = []
subject_list = []

student_list = []

# факультеты
for item in faculty_names:
    faculty = Faculty(name=item)
    db.add(faculty)
db.commit()
db.close()

faculty_list = get_all_faculty()
# print(*faculty_list, sep='')

# корпуса
for item in housing_names:
    housing = Housing(name=item)
    arr = gen_arr(faculty_list)

    # for i in arr:
    #     housing.faculty.append(faculty_list[i])
    #
    db.add(housing)
db.commit()
db.close()

housing_list = get_all_housing()
# print(*housing_list, sep='')


# группы
for item in group_by_course_names:
    for it in item:
        course = int(it.split(':')[1]) + 1
        group = Group(name=it, course=course)

        db.add(group)
db.commit()
db.close()

group_list = get_all_group()
# print(*group_list, sep='')


# предметы
for sub in academic_subject:
    subject = Subject(name=sub)

    db.add(subject)
db.commit()
db.close()

subject_list = get_all_subject()
print(*subject_list, sep='')
