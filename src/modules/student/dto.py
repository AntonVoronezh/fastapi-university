from fastapi_camelcase import CamelModel
from pydantic import BaseModel


class StudentBaseDto(CamelModel):
    first_name: str
    second_name: str
    family: str
    age: int


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
