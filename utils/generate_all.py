from faker import Faker


from db.db import SessionLocal, engine, Base
from utils.generate_tables import Faculty, Student

fake = Faker('ru_RU')
db = SessionLocal()


housing_names = ['Alfa', 'Bravo', 'Charly', 'Ecco', 'Delta']
faculty_names = [
    'Факультет географии',
    'Факультет экологии ',
    'Факультет туризма',
    'Факультет журналистики',
    'Факультет Истории',
    'Факультет математики',
    'Факультет биологии',
    'Факультет физики',
    'Факультет философии',
]

faculty_list = []

for f in faculty_names:
    housing = fake.random.choices(housing_names)[0]
    faculty = Faculty(name=f, housing=housing)

    db.add(faculty)
    faculty_list.append(faculty)

# print(*faculty_list, sep='\n')

db.commit()

for _ in range(100):
    name = fake.name()
    address = fake.address()
    age = fake.random.randint(18, 25)
    course = fake.random.randint(1, 5)
    group = fake.random.randint(1, 10)
    faculty_id = fake.random.choices(faculty_list)[0].id

    student = Student(name=name, address=address, age=age, course=course, group=group, faculty_id=faculty_id)
    # print(student)
    db.add(student)

db.commit()

db.close()


#
#
# lessons_names = ['Математика', 'Программирование', 'Философствуем за кружечкой пенного',
#                  'Алгоритмы и структуры данных', 'Линейная алгебра', 'Мат. статистика',
#                  'Физкультура']
# group1 = Group(group_name='1-МДА-7')
# group2 = Group(group_name='1-МДА-9')
# session.add(group1)
# session.add(group2)
#
# for key, it in enumerate(lessons_names):
#     lesson = Lesson(lesson_title=it)
#     lesson.groups.append(group1)
#     if key % 2 == 0:
#         lesson.groups.append(group2)
#     session.add(lesson)
#
# faker = Faker('ru_RU')
# group_list = [group1, group2]
# session.commit()
#
# for _ in range(50):
#     full_name = faker.name().split(' ')
#     age = faker.random.randint(16, 25)
#     address = faker.address()
#     group = faker.random.choice(group_list)
#     student = Student(full_name, age, address, group.id)
#     session.add(student)
