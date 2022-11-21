from pydantic import BaseModel


class StudentBaseDto(BaseModel):
    name: str
    address: str
    age: int
    course: int
    group: int


class StudentDTO(StudentBaseDto):
    id: int

    class Config:
        orm_mode = True
