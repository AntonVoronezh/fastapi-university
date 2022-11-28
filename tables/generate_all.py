from faker import Faker
from random import randint

from db.db import SessionLocal
from tables.generate_tables import Faculty, Housing, Group
from tables.watch import get_all_faculty, get_all_housing

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

# db.commit()
#
# for f, g in enumerate(faculty_list):
#     for i in range(7):
#         # name = g.name.split(' ')
#         # name_f = f'{name[0][0:3].upper()}-{name[1][0:4].upper()}-{i + 1}'
#         # group = Group(name=name_f, faculty_id=g.id, housing_id=)
#         print(len(g.housing))
#         print(g.name)
#         # group_list.append(group)
#         # db.add(group)
#
# # print(*housing_list, sep='\n')
#


# db.commit()
# db.close()
