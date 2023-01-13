from pydantic import BaseModel


class StudentInfoBaseDto(BaseModel):
    student_id: int
    description: str
    address: str


class StudentInfoDTO(StudentInfoBaseDto):
    id: int

    class Config:
        orm_mode = True
