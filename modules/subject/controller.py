from http.client import HTTPException

from db.db import db
from modules.subject.dto_plus_groups import SubjectPlusGroupsDTO

from shared.controllers import api_router_factory
from models.subject import Subject

subjects_router = api_router_factory("subjects")


@subjects_router.get('/', response_model=list[SubjectPlusGroupsDTO], status_code=200,
                     name='Получение всех предметов')
def get_all_subjects() -> list[SubjectPlusGroupsDTO]:
    faculties = db.query(Subject).all()
    return faculties


@subjects_router.get('/{id}', response_model=SubjectPlusGroupsDTO, status_code=200, name='Получение предмета')
def get_subject(id: int) -> SubjectPlusGroupsDTO:
    faculty = db.query(Subject).filter(Subject.id == id).first()

    return faculty

