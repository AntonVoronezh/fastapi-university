from fastapi import Depends
from sqlalchemy.orm import Session

from src.db.db import get_session
from src.models import Student

from src.modules.student.dto import StudentCreateDTO, StudentUpdateDTO

from src.shared.base_service import BaseService


class StudentService(BaseService[Student, StudentCreateDTO, StudentUpdateDTO]):
    def __init__(self, db_session: Session):
        super(StudentService, self).__init__(Student, db_session)


def get_student_service(db_session: Session = Depends(get_session)) -> StudentService:
    return StudentService(db_session)