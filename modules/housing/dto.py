from pydantic import BaseModel

from modules.group.dto import GroupDTO


class HousingBaseDto(BaseModel):
    name: str
    faculty_id: int | None
    groups: list[GroupDTO]


class HousingDTO(HousingBaseDto):
    id: int

    class Config:
        orm_mode = True
