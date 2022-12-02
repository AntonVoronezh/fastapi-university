from pydantic import BaseModel

from modules.student.info_dto import StudentInfoDTO


class StudentBaseDto(BaseModel):
    first_name: str
    second_name: str
    family: str
    age: int
    group_id: int or None


class StudentBasePlusInfoDto(StudentBaseDto):
    info: StudentInfoDTO


class StudentDTO(StudentBasePlusInfoDto):
    id: int

    class Config:
        orm_mode = True


class StudentBaseUpdateDto(BaseModel):
    first_name: str or None
    second_name: str or None
    family: str or None
    age: int or None
    group_id: int or None

    class Config:
        orm_mode = True
