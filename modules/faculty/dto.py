from pydantic import BaseModel

from modules.group.dto import GroupDTO
from modules.housing.dto import HousingDTO


class FacultyBaseDto(BaseModel):
    name: str
    groups: list[GroupDTO]
    housings: list[HousingDTO]


class FacultyDTO(FacultyBaseDto):
    id: int

    class Config:
        orm_mode = True


