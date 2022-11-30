

from modules.group.dto import GroupBaseDto
from modules.subject.dto import SubjectDTO


class GroupBasePlusSubjectsDto(GroupBaseDto):
    subjects: list[SubjectDTO] = []


class GroupPlusSubjectsDTO(GroupBasePlusSubjectsDto):
    id: int

    class Config:
        orm_mode = True


