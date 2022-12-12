from fastapi import Depends
from sqlalchemy.orm import Session

from modules.subject.dto_plus_groups import SubjectPlusGroupsCreateDTO, SubjectPlusGroupsUpdateDTO
from db.db import get_session
from models.subject import Subject

from shared.base_service import BaseService


class SubjectService(BaseService[Subject, SubjectPlusGroupsCreateDTO, SubjectPlusGroupsUpdateDTO]):
    def __init__(self, db_session: Session):
        super(SubjectService, self).__init__(Subject, db_session)


def get_subject_service(db_session: Session = Depends(get_session)) -> SubjectService:
    return SubjectService(db_session)
