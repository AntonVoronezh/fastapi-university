from faker import Faker
from random import randint

from db.db import SessionLocal
from tables.generate_tables import Faculty, Student, StudentInfo, Housing

fake = Faker('ru_RU')
db = SessionLocal()

def gen_arr(in_list):
    ran = randint(1, 5)
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
     'Факультет психологии', 'Факультет права','Факультет юриспруденции', 'Факультет экономики',
     'Факультет геологии', 'Факультет отношений'
]

faculty_list = []
student_list = []
housing_list = []

for f in faculty_names:
    # housing = fake.random.choices(housing_names)[0]
    faculty = Faculty(name=f)

    # db.add(faculty)
    faculty_list.append(faculty)


# print(*faculty_list, sep='\n')

# db.commit()


for h in housing_names:
    housing = Housing(name=h)
    arr = gen_arr(faculty_list)

    for i in arr:
        housing.faculty.append(faculty_list[i])

    db.add(housing)
    housing_list.append(housing)

# print(*housing_list, sep='\n')

db.commit()


for _ in range(100):
    name = fake.name().split(' ')
    course = fake.random.randint(1, 5)
    group = fake.random.randint(1, 10)
    faculty_id = fake.random.choices(faculty_list)[0].id

    student = Student(first_name=name[0], second_name=name[1], family=name[2], course=course, group=group,
                      faculty_id=faculty_id)
    # print(student)
    db.add(student)
    student_list.append(student)

db.commit()

for i, s in enumerate(student_list):
    address = fake.address()
    age = fake.random.randint(18, 25)

    if i % 3 == 0:
        student_info = StudentInfo(address=None, age=None, student_id=s.id)
    else:
        student_info = StudentInfo(address=address, age=age, student_id=s.id)

    # print(student_info)
    db.add(student_info)

db.commit()

db.close()
