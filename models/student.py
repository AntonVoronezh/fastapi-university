from pydantic import BaseModel

from models.student_info import StudentInfoDTO


class StudentBaseDto(BaseModel):
    first_name: str
    second_name: str
    family: str
    course: int
    group: int
    faculty_id: int
    info: StudentInfoDTO


class StudentDTO(StudentBaseDto):
    id: int

    class Config:
        orm_mode = True
