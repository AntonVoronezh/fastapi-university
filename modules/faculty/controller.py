from http.client import HTTPException

from db.db import db
from modules.faculty.dto import FacultyDTO

from shared.controllers import api_router_factory
from tables.generate_tables import Faculty

faculties_router = api_router_factory("faculties")


@faculties_router.get('/', response_model=list[FacultyDTO], status_code=200,
                     name='Получение всех факультетов')
def get_all_faculties():
    faculties = db.query(Faculty).all()
    return faculties


@faculties_router.get('/{id}', response_model=FacultyDTO, status_code=200, name='Получение факультета')
def get_faculty(id: int):
    faculty = db.query(Faculty).filter(Faculty.id == id).first()

    return faculty

#
# @faculties_router.post('/', response_model=FacultyWithStudentsDTO, status_code=201, name='Запись нового факультета')
# def create_faculty(item: FacultyBaseWithStudentsDto):
#     faculty = db.query(Faculty).filter(Faculty.name == item.name).first()
#
#     if faculty is not None:
#         return HTTPException(status_code=400, detail='Не существует')
#
#     new_faculty = Faculty(name=item.name, housing=item.housing)
#
#     db.add(new_faculty)
#     db.commit()
#
#     return new_faculty
#
#
# @faculties_router.put('/{id}', response_model=FacultyWithStudentsDTO, status_code=200, name='Обновление факультета')
# def update_faculty(id: int, item: FacultyBaseWithStudentsDto):
#     faculty_to_update = db.query(Faculty).filter(Faculty.id == id).first()
#
#     faculty_to_update.name = item.name
#     faculty_to_update.housing = item.housing
#
#     db.commit()
#
#     return faculty_to_update
#
#
# @faculties_router.delete('/{id}', status_code=204, name='Удаление факультета')
# def delete_faculty(id: int):
#     faculty_to_delete = db.query(Faculty).filter(Faculty.id == id).first()
#
#     if faculty_to_delete is None:
#         raise HTTPException(status_code=404, detail='факультет не найден')
#
#     db.delete(faculty_to_delete)
#     db.commit()
#
#     return faculty_to_delete

