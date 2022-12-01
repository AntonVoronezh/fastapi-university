from pydantic import BaseModel


class StudentInfoBaseDto(BaseModel):
    student_id: int
    description: str or None
    img: str or None
    address: str or None


class StudentInfoDTO(StudentInfoBaseDto):
    id: int

    class Config:
        orm_mode = True
