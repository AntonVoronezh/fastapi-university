from fastapi import Depends

from modules.faculty.dto import FacultyDTO
from modules.faculty.service import FacultyService, get_faculty_service

from shared.controllers import api_router_factory

faculties_router = api_router_factory("faculties")


@faculties_router.get('/', response_model=list[FacultyDTO], status_code=200, name='Получение всех факультетов')
def get_all_faculties(faculty_service: FacultyService = Depends(get_faculty_service)) -> list[FacultyDTO]:
    return faculty_service.list()


@faculties_router.get('/{id}', response_model=FacultyDTO, status_code=200, name='Получение факультета')
def get_faculty(id: int, faculty_service: FacultyService = Depends(get_faculty_service)) -> FacultyDTO:
    return faculty_service.get(id)


