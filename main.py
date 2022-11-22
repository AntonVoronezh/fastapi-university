# uvicorn main:app --reload
from fastapi import FastAPI, status

from db.db import SessionLocal
from models.student import StudentDTO
from utils.generate_student import Student
from models.student import StudentBaseDto

app = FastAPI()
db = SessionLocal()


#
# for it in db.query(Student):
#     print(it.name)

@app.get('/students', response_model=list[StudentDTO], status_code=status.HTTP_200_OK, name='Получение всех студентов')
def get_all_students():
    students = db.query(Student).all()
    return students


@app.get('/students/{student_id}', response_model=StudentDTO, status_code=200, name='Получение студента')
def get_student_by_id(student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()

    return student


@app.post('/students', response_model=StudentDTO, status_code=201, name='Запись нового студента')
def create_student(item: StudentBaseDto):
    student = db.query(Student).filter(Student.name == item.name).first()

    if student is not None:
        return HTTPException(status_code=400, detail='Не существует')

    new_student = Student(name=item.name, address=item.address, age=item.age, course=item.course, group=item.group)

    db.add(new_student)
    db.commit()

    return new_student


@app.put('/students/{student_id}', response_model=StudentDTO, status_code=200, name='Обновление студента')
def update_student_by_id(student_id: int, item: StudentBaseDto):
    student_to_update = db.query(Student).filter(Student.id == student_id).first()

    student_to_update.name = item.name
    student_to_update.address = item.address
    student_to_update.age = item.age
    student_to_update.course = item.course
    student_to_update.group = item.group

    db.commit()

    return student_to_update


@app.delete('/item/{student_id}')
def delete_student_by_id(student_id: int):
    student_to_delete = db.query(Student).filter(Student.id == student_id).first()

    if student_to_delete is None:
        raise HTTPException(status_code=404, detail='Студент не найден')

    db.delete(student_to_delete)
    db.commit()

    return student_to_delete
