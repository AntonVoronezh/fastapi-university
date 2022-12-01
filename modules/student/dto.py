from pydantic import BaseModel


class StudentBaseDto(BaseModel):
    first_name: str
    second_name: str
    family: str
    age: int


class StudentDTO(StudentBaseDto):
    id: int

    class Config:
        orm_mode = True
