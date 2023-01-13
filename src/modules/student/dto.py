from fastapi_camelcase import CamelModel
from pydantic import BaseModel

from src.modules.student_info.dto import StudentInfoDTO


class StudentBaseDto(CamelModel):
    first_name: str
    second_name: str
    family: str
    age: int
    info: StudentInfoDTO


class StudentDTO(StudentBaseDto):
    id: int

    class Config:
        orm_mode = True


class StudentBaseUpdateDto(BaseModel):
    first_name: str | None
    second_name: str | None
    family: str | None
    age: int | None

    class Config:
        orm_mode = True


class StudentCreateDTO(StudentBaseDto):
    pass


class StudentUpdateDTO(StudentBaseDto):
    pass
