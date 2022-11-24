from pydantic import BaseModel, validator, Field


class StudentInfoBaseDto(BaseModel):
    age: int or None = Field(default=None)
    address: str or None = Field(default=None)

    @validator("age")
    def parse_age(cls, value):
        return value or None

    @validator("address")
    def parse_address(cls, value):
        return value or None


class StudentInfoDTO(StudentInfoBaseDto):
    id: int

    class Config:
        orm_mode = True
