from pydantic import BaseModel

from modules.faculty.info_dto import FacultyInfoDTO
from modules.group.dto import GroupDTO
from modules.housing.dto import HousingDTO


class FacultyBaseDto(BaseModel):
    name: str
    groups: list[GroupDTO]
    housings: list[HousingDTO]
    info: FacultyInfoDTO


class FacultyDTO(FacultyBaseDto):
    id: int

    class Config:
        orm_mode = True


