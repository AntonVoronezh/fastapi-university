from pydantic import BaseModel

from models.student import StudentDTO
from utils.generate_tables import Student


class FacultyBaseDto(BaseModel):
    name: str
    housing: str
    students: list[StudentDTO] = []


class FacultyDTO(FacultyBaseDto):
    id: int

    class Config:
        orm_mode = True
