from pydantic import BaseModel

from modules.student.info_dto import StudentInfoDTO


class StudentBaseDto(BaseModel):
    first_name: str
    second_name: str
    family: str
    age: int
    info: StudentInfoDTO
    group_id: int or None


class StudentDTO(StudentBaseDto):
    id: int

    class Config:
        orm_mode = True
