from http.client import HTTPException
from fastapi import status

from db.db import db
from models.faculty import FacultyDTO, FacultyBaseDto
from shared.controllers import api_router_factory
from utils.generate_tables import Faculty

faculties_router = api_router_factory("faculties")


@faculties_router.get('/', response_model=list[FacultyDTO], status_code=200,
                     name='Получение всех факультетов')
def get_all_faculties():
    faculties = db.query(Faculty).all()
    faculties = db.query(Faculty).all()
    return faculties


@faculties_router.get('/{faculty_id}', response_model=FacultyDTO, status_code=200, name='Получение факультета')
def get_student_by_id(faculty_id: int):
    faculty = db.query(Faculty).filter(Faculty.id == faculty_id).first()

    return faculty


@faculties_router.post('/', response_model=FacultyDTO, status_code=201, name='Запись нового факультета')
def create_student(item: FacultyBaseDto):
    faculty = db.query(Faculty).filter(Faculty.name == item.name).first()

    if faculty is not None:
        return HTTPException(status_code=400, detail='Не существует')

    new_faculty = Faculty(name=item.name, housing=item.housing)

    db.add(new_faculty)
    db.commit()

    return new_faculty


@faculties_router.put('/{faculty_id}', response_model=FacultyDTO, status_code=200, name='Обновление факультета')
def update_student_by_id(faculty_id: int, item: FacultyBaseDto):
    faculty_to_update = db.query(Faculty).filter(Faculty.id == faculty_id).first()

    faculty_to_update.name = item.name
    faculty_to_update.housing = item.housing

    db.commit()

    return faculty_to_update


@faculties_router.delete('/{faculty_id}')
def delete_student_by_id(faculty_id: int):
    faculty_to_delete = db.query(Faculty).filter(Faculty.id == faculty_id).first()

    if faculty_to_delete is None:
        raise HTTPException(status_code=404, detail='факультет не найден')

    db.delete(faculty_to_delete)
    db.commit()

    return faculty_to_delete
