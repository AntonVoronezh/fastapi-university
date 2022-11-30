from modules.group.dto import GroupDTO
from modules.subject.dto import SubjectBaseDto


class SubjectBasePlusGroupsDto(SubjectBaseDto):
    groups: list[GroupDTO] = []


class SubjectPlusGroupsDTO(SubjectBasePlusGroupsDto):
    id: int

    class Config:
        orm_mode = True


