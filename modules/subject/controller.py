from http.client import HTTPException
from fastapi import Depends
from db.db import db
from modules.subject.dto_plus_groups import SubjectPlusGroupsDTO
from modules.subject.service import SubjectService, get_subject_service
from shared.controllers import api_router_factory
from models.subject import Subject

subjects_router = api_router_factory("subjects")


@subjects_router.get('/', response_model=list[SubjectPlusGroupsDTO], status_code=200,
                     name='Получение всех предметов')
def get_all_subjects(subject_service: SubjectService = Depends(get_subject_service)) -> list[SubjectPlusGroupsDTO]:
    return subject_service.list()


@subjects_router.get('/{id}', response_model=SubjectPlusGroupsDTO, status_code=200, name='Получение предмета')
def get_subject(id: int, subject_service: SubjectService = Depends(get_subject_service)) -> SubjectPlusGroupsDTO:
    return subject_service.get(id)

