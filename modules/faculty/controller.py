from db.db import db
from models.faculty import Faculty
from modules.faculty.dto import FacultyDTO

from shared.controllers import api_router_factory

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


