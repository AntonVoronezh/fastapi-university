from pydantic import BaseModel

from models.student import StudentDTO


class FacultyBaseDto(BaseModel):
    name: str
    housing: str
    students: list[StudentDTO] = []


class FacultyDTO(FacultyBaseDto):
    id: int

    class Config:
        orm_mode = True
