from pydantic import BaseModel


class FacultyBaseDto(BaseModel):
    name: str
    housing: str


class FacultyDTO(FacultyBaseDto):
    id: int

    class Config:
        orm_mode = True
