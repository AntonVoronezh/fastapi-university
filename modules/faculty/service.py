from fastapi import Depends
from sqlalchemy.orm import Session

from db.db import get_session
from models import Faculty
from modules.faculty.dto import FacultyCreateDTO, FacultyUpdateDTO

from shared.base_service import BaseService


class FacultyService(BaseService[Faculty, FacultyCreateDTO, FacultyUpdateDTO]):
    def __init__(self, db_session: Session):
        super(FacultyService, self).__init__(Faculty, db_session)


def get_faculty_service(db_session: Session = Depends(get_session)) -> FacultyService:
    return FacultyService(db_session)
