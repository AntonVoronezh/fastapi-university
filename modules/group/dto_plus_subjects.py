

from modules.group.dto import GroupBaseDto
from modules.student.dto import StudentDTO
from modules.subject.dto import SubjectDTO


class GroupBasePlusSubjectsDto(GroupBaseDto):
    subjects: list[SubjectDTO] = []
    students: list[StudentDTO] = []


class GroupPlusSubjectsDTO(GroupBasePlusSubjectsDto):
    id: int

    class Config:
        orm_mode = True


