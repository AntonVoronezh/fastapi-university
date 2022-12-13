from pydantic import BaseModel

from modules.student.info_dto import StudentInfoDTO


class StudentBaseDto(BaseModel):
    first_name: str
    second_name: str
    family: str
    age: int
    group_id: int | None


class StudentBasePlusInfoDto(StudentBaseDto):
    info: StudentInfoDTO


class StudentDTO(StudentBasePlusInfoDto):
    id: int

    class Config:
        orm_mode = True


class StudentBaseUpdateDto(BaseModel):
    first_name: str | None
    second_name: str | None
    family: str | None
    age: int | None
    group_id: int | None

    class Config:
        orm_mode = True


class StudentCreateDTO(StudentBaseDto):
    pass


class StudentUpdateDTO(StudentBaseDto):
    pass
