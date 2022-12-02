from http.client import HTTPException
from fastapi import Body

from db.db import db
from models.student import Student
from models.student_info import StudentInfo
from modules.student.dto import StudentDTO, StudentBasePlusInfoDto, StudentBaseDto, StudentBaseUpdateDto
from shared.controllers import api_router_factory


student_router = api_router_factory("student")


@student_router.get('/', response_model=list[StudentDTO], status_code=200,
                     name='Получение всех студентов')
def get_all_student():
    students = db.query(Student).all()
    return students


@student_router.get('/{id}', response_model=StudentDTO, status_code=200, name='Получение студента')
def get_student(id: int):
    student = db.query(Student).filter(Student.id == id).first()

    return student


@student_router.post('/', response_model=StudentDTO, status_code=201, name='Запись нового студента')
def create_student(item: StudentBaseDto = Body()):
    new_student = Student(first_name=item.first_name, second_name=item.second_name,
                          family=item.family, age=item.age, group_id=item.group_id)
    new_student.info = StudentInfo(description='description', img='img', student_id=1, address='address')

    db.add(new_student)
    db.commit()

    return new_student


@student_router.put('/{id}', response_model=StudentDTO, status_code=200, name='Обновление студента')
def update_student(id: int, item: StudentBaseUpdateDto = Body()):
    student_to_update = db.query(Student).filter(Student.id == id).first()

    student_to_update.first_name = item.first_name
    student_to_update.second_name = item.second_name
    student_to_update.family = item.family
    student_to_update.age = item.age
    student_to_update.group_id = item.group_id

    db.commit()
    return student_to_update


@student_router.delete('/{id}', status_code=204, name='Удаление студента')
def delete_student(id: int):
    student_to_delete = db.query(Student).filter(Student.id == id).first()

    if student_to_delete is None:
        raise HTTPException(status_code=404, detail='факультет не найден')

    db.delete(student_to_delete)
    db.commit()
    db.close()
    return student_to_delete

