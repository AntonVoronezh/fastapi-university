from pydantic import BaseModel

from modules.group.dto import GroupDTO


class FacultyBaseDto(BaseModel):
    name: str
    groups: list[GroupDTO]


class FacultyDTO(FacultyBaseDto):
    id: int

    class Config:
        orm_mode = True


