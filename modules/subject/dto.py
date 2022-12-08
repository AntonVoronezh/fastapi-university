from pydantic import BaseModel


class SubjectBaseDto(BaseModel):
    name: str


class SubjectDTO(SubjectBaseDto):
    id: int

    class Config:
        orm_mode = True
