from pydantic import BaseModel


class FacultyInfoBaseDto(BaseModel):
    description: str or None
    img: str or None
    faculty_id: int


class FacultyInfoDTO(FacultyInfoBaseDto):
    id: int

    class Config:
        orm_mode = True
